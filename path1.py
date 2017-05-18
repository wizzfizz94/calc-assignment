# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import networkx as nx
import matplotlib.pyplot as plt
import random
import time

class Path1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://teaching.csse.uwa.edu.au/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_path1(self):
        driver = self.driver
        driver.get(self.base_url + "/units/CITS5501/Assignments/calculator.html")
        g = createTestGraph()
        ppaths = getPrimePaths(g)
        last = None
        for i in range(len(ppaths)):
            if ppaths[i][0] == last || last == None:
                for j in range(len(ppaths[i])):
                    if ppaths[i][j] == 'num':
                        clickNum(driver)
                    elif ppaths[i][j] == 'op':
                        clickOp(driver)
                    elif ppaths[i][j] == 'eql':
                        driver.find_element_by_id("eqn-bg").click()
                    elif ppaths[i][j] == 'del':
                        driver.find_element_by_id("delete").click()
                    elif ppaths[i][j] == 'zero':
                        driver.find_element_by_css_selector("div.rows > #delete").click()
                    elif ppaths[i][j] == 'period':
                        driver.find_element_by_xpath("//button[@value='.']").click()
                    elif ppaths[i][j] == '0':
                        time.sleep(1)
                    if j == len(ppaths[i])-1:
                        last = ppaths[i][j]
                    time.sleep(0.5)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


def is_a_in_x(A, X):
  for i in xrange(len(X) - len(A) + 1):
    if A == X[i:i+len(A)]: return True
  return False

def removeSubPaths(sp):
    # mark all sub paths as None
    for i in range(len(sp)):
        for j in range(len(sp)):
            if sp[i] != None and sp[j] != None and j != i:
                if is_a_in_x(sp[i], sp[j]):
                    sp[i] = None
                elif is_a_in_x(sp[j], sp[i]):
                    sp[j] = None
    # clear all none entries
    return [x for x in sp if x is not None]

def genEdgesToRootNodes(nodes):
    edges = []
    for x in nodes:
        edges.extend([(x, 'num'), (x, 'op'),
            (x, 'del'), (x, '.'), (x, '=')])
    return edges


def createDeleteGraph():
    g = nx.Graph()
    g.add_edges_from(genEdgesToRootNodes(['num', 'op', 'del', '.', '=']),
                     name='concat('')')
    return g

def createOperatorGraph():
    g = nx.Graph()
    g.add_node('op')
    g.add_node('output')
    g.add_edge('op', 'operator', name=None)
    g.add_edges_from(genEdgesToRootNodes(['op']), name='concat('')')
    g.add_edges_from(genEdgesToRootNodes(['output']), name='concat(operator)')
    g.add_edges_from(genEdgesToRootNodes(['output']), name=None)
    return g

def makeGraph(nodes):
    g = nx.Graph()
    g.add_nodes_from(nodes)
    for i in nodes:
        for j in nodes:
            g.add_edge(i,j)
    return g

def multiconnect(g, n1, n2):
    g.add_edge(n1,n2)
    g.add_edge(n2,n1)

def getPrimePaths(g):
    paths = []
    for i in g.nodes_iter():
        for j in g.nodes_iter():
            paths.extend(nx.all_simple_paths(g,i,j))
    return removeSubPaths(paths)

def clickNum(driver):
    driver.find_element_by_xpath("//button[@value='"+str(random.randint(0,9))+"']").click()

def clickOp(driver):
    ops = ['+', '/', '%', '-', '*']
    driver.find_element_by_xpath("//button[@value='"+random.choice(ops)+"']").click()

def createTestGraph():
    print 'graph for basic calc use case'
    g2 = nx.MultiDiGraph()
    g2.add_nodes_from(['0', 'num', 'zero', 'period', 'op', 'eql', 'del'])
    g2.add_edges_from([('0', 'num'), ('0', 'zero'), ('num', 'eql'), ('zero', 'eql'), ('eql', '0'), ('del', '0')])
    multiconnect(g2,'num','zero')
    multiconnect(g2, 'num', 'op')
    multiconnect(g2, 'num', 'period')
    multiconnect(g2, 'op', 'zero')
    multiconnect(g2, 'period', 'zero')
    g2.add_edges_from([('period', 'del'), ('num', 'del'), ('zero', 'del'), ('op', 'del')])
    ppaths = getPrimePaths(g2)
    for path in ppaths:
        print path
    print '# of primepaths = ' + str(len(ppaths))
    nx.draw_networkx(g2)
    labels = {'0': '0', 'num': 'num', 'op': 'op'}
    plt.show()
    return g2

if __name__ == "__main__":
    createTestGraphs()
    unittest.main()
