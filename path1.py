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
        ele = driver.find_element_by_xpath("//button[@value='8']").click()
        driver.find_element_by_xpath("//button[@value='+']").click()
        driver.find_element_by_xpath("//button[@value='9']").click()
        driver.find_element_by_id("eqn-bg").click()
        self.assertEqual("17", driver.find_element_by_id("result").text)
    
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

def getPrimePaths(sp):
    # primePaths = [row[:] for row in simplePaths]
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

def

def createTestGraphs():
    # user performs basic calc

    # user performs decimal calc

    # user perofms mult-step calc

    # user clears screen with del

    # user alerted after inputing to many numbers

    # invalid inputs are handled
    
    g = nx.Graph()
    nodes = ['num1', 'num2', 'eql', 'zero', 'op']
    g.add_nodes_from(nodes)
    for i in nodes:
        for j in nodes:
            g.add_edge(i,j)
    print g.edges()
    simplePaths = list(nx.all_simple_paths(g, source='num1', target='eql'))
    # for i in nodes:
    #     simplePaths.extend(list(nx.all_simple_paths(g, source='num', target=i)))
    primePaths = getPrimePaths(simplePaths)
    for path in primePaths:
        print path
    print len(primePaths)
    print len(simplePaths)
    nx.draw(g)
    plt.show()
    return g

if __name__ == "__main__":
    createTestGraphs()
    unittest.main()
