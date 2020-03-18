import yaml

class Sala():
    def __init__(self, id, tenant):
        self.__config = yaml.load(open('./Scripts/config.yaml', 'r'))
        self.__msg = None
        self.__id = id
        self.__tenant = tenant
        self.__nodes = []
        print(self.__config['Nodes'])
        for x in self.__config['Nodes']:
            node = {'ID': x['ID'], 'Status': False}
            self.__nodes.append(node)

    def get_nodes(self):
        return self.__nodes

    def get_allNodes(self):
        for node in self.__nodes:
            if not node['Status']:
                return 0
        print(self.__nodes)
        return 1

    def get_oneNode(self):
        for node in self.__nodes:
            if node['Status']:
                return 1
        return 0

    def set_node(self, status, index):
        self.__nodes[index]['Status'] = status

    def set_allNodes(self):
        for x in range(len(self.__nodes)):
            self.__nodes[x]['Status'] = False
        #print(self.__nodes)
