#from selenium import webdriver
from bs4 import BeautifulSoup
from Graph import Graph, Page_Node
from helpers import validate_url, is_valid, remove_duplicates
import requests
from collections import deque

# can set the max urls based on the depth chosen on website?
# just using 10 to test right now 
MAX_URLS = 10

class Spider:
    def __init__(self, seed_url, search_type, limit):
        #self.driver = webdriver.Firefox()
        self.seed_url = seed_url
        self.search_type = search_type # 'BFS' or 'DFS'
        self.count = 0
        self.limit = int(limit) # number of pages to crawl (number of nodes)
        self.depth = 0 # used for DFS
        self.to_visit = deque() # list of urls to crawl
        self.visited_set = set()   # set of urls already crawled
        self.graph = Graph()
        self.id = 0
        self.url_graph = dict() # store graph/node info
        self.start_page = self.get_page_title(seed_url)
        root_node = Page_Node(seed_url, None, self.start_page, 0, None, 0)
        self.start(root_node)
        
    
    # generate soup
    def get_soup(self, url):
        response = requests.get(url)
        # lxml faster than html_parser..?
        data = response.text
        soup = BeautifulSoup(data, "lxml")
        return soup
        '''
        #if using selenium:
        self.driver.get(url)
        soup = BeautifulSoup(self.driver.page_source, "lxml")
        return soup
        '''
    # parse soup to get links
    def get_links(self, url):
        soup = self.get_soup(url)
        urls = set()
        for link in soup.findAll('a'):
            if self.havent_visited(link):
                urls.add(link.get('href'))
        return urls


    # parse soup for page title
    def get_page_title(self, url):
        soup = self.get_soup(url)
        title = soup.title
        if title is not None:
            return title.get_text()
    
    def havent_visited(self, url):
        if url not in self.visited_set and url not in self.to_visit:
            return True
        else: return False

    #  start the crawling
    def start(self, node):
        self.to_visit.clear()
        self.visited_set.clear()
        
        if self.search_type == 'BFS':
            self.bfs_crawl(node)
        else:
            self.dfs_crawl(node)

    #BFS
    def bfs_crawl(self, node):
        # check that the url has not be crawled
        crawled = node.url in self.visited_set
        if not crawled:
            self.graph.add_node(node, self.id)
            self.count += 1
            self.id += 1
            self.visited_set.add(node.url)
        # node has parent
        if node.parents_list:
            # get the node's parent node
            source_node = node.parents_list.pop()
            # update the node depth
            node.node_depth = source_node.node_depth
            if node.id is not None and source_node.id is not None:
                # create an edge between the current node and its parent node
                self.graph.add_edge(source_node.id, node.id)
            # set node's parent node
            node.parent_node = source_node.id
        if not crawled:
            # generate soup and get links
            links = self.get_links(node.url)
            links = validate_url(links, self.count, MAX_URLS)
            # remove any duplicate links present
            links = remove_duplicates(links)
            if len(links) > 0:
                self.crawl(node, links)
            else:
                self.get_next()
        else:
            self.get_next()
    
    #DFS
    def dfs_crawl(self, node):
        crawled = node.url in self.visited_set
        if not crawled:
            self.graph.add_node(node, self.id)
            self.count += 1
            self.id += 1
            self.visited_set.add(node.url)
        if node.parents_list:
            source_node = node.parents_list.pop()
            node.node_depth = self.depth
            if node.id is not None and source_node.id is not None:
                self.graph.add_edge(source_node.id, node.id)
            node.parent_node = source_node.id
        if not crawled:
            links = self.get_links(node.url)
            links = validate_url(links, self.count, MAX_URLS)
            links = remove_duplicates(links)
            if len(links) > 0:
                if self.depth < self.limit:
                    self.depth += 1
                    self.crawl(node, links)
                # if depth limit has been reached
                else:
                    self.depth = 0
                    node.node_depth = 1
                    self.get_next()
            # no links left to crawl
            else:
                self.get_next()
        else:
            self.get_next()

    '''Urls are added to the right of the deque (append)
    Difference between the two algos BFS and DFS: how urls are popped off'''
    def crawl(self, current_url, links):
        for link in links:
            if link not in self.visited_set:
                title = self.get_page_title(link)
                current_node = Page_Node(link, [current_url], title, self.depth)
                # add url to end of list source nodes list
                current_node.parents_list.append(current_url)
                # add to the end of the to_visit list
                self.to_visit.append(current_node)
                self.url_graph[link] = current_node
        self.get_next()

    def get_next(self):
        if len(self.to_visit) > 0 and self.count < MAX_URLS:
            # BFS: queue - url popped off from left; FIFO
            if self.search_type == 'BFS':
                next_node = self.to_visit.popleft()
                self.bfs_crawl(next_node)
            # DFS: stack - url popped off from right; LIFO
            else:
                next_node = self.to_visit.pop()
                self.dfs_crawl(next_node)
        else: self.end_crawl()

    #used for testing
    def print_data(self):
        # print nodes dict
        print("\n--------Page Nodes--------" )
        for node in self.graph.nodes:
            node.jsonify()
        # print the graph edges
        if self.graph.edges:
            print("\n-----Graph Edges-----")
            print("Parent ID ---> Target ID")
            edge_count = 0
            for edge in self.graph.edges:
                print(str(edge.parent) +" ----> " +  str(edge.target))
                edge_count += 1
            print("Number of edges: ", edge_count)

    def end_crawl(self):
        self.print_data()
        #self.driver.close()
  

