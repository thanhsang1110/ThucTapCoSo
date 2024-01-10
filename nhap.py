import csv

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex, neighbors):
        self.graph[vertex] = neighbors

    def get_neighbors(self, vertex):
        if vertex in self.graph:
            return self.graph[vertex]
        else:
            return []

class DFS_Graph(Graph):
    def dfs_search(self, start_vertex, target_vertex):
        visited = set()
        stack = [start_vertex]

        while stack:
            current_vertex = stack.pop()
            if current_vertex == target_vertex:
                return True
            visited.add(current_vertex)
            neighbors = self.get_neighbors(current_vertex)
            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
        
        return False

class BFS_Graph(Graph):
    def bfs_search(self, start_vertex, target_vertex):
        visited = set()
        queue = [start_vertex]

        while queue:
            current_vertex = queue.pop(0)
            if current_vertex == target_vertex:
                return True
            visited.add(current_vertex)
            neighbors = self.get_neighbors(current_vertex)
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
        
        return False

class GraphReader:
    @staticmethod
    def read_from_csv(file_path):
        graph = Graph()
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                vertex = row[0]
                neighbors = row[1:]
                graph.add_vertex(vertex, neighbors)
        return graph

if __name__ == "__main__":
    graph = Graph()

    choice = input("Chọn lựa chọn:\n1. Đọc đồ thị từ file CSV\n2. Nhập đồ thị từ bàn phím\n")
    while choice not in ['1', '2']:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
        choice = input("Chọn lựa chọn:\n1. Đọc đồ thị từ file CSV\n2. Nhập đồ thị từ bàn phím\n")
    
    if choice == '1':
        while True:
            file_path = input("Nhập đường dẫn đến file CSV: ")
            try:
                graph = GraphReader.read_from_csv(file_path)
                break
            except FileNotFoundError:
                print("File không tồn tại. Vui lòng nhập lại.")
    elif choice == '2':
        num_vertices = int(input("Nhập số lượng đỉnh: "))
        for i in range(num_vertices):
            vertex = input("Nhập đỉnh: ")
            neighbors = input("Nhập danh sách đỉnh kề, phân tách bằng dấu cách (nếu không có, hãy nhập dấu gạch ngang '-'): ")
            while neighbors != '-' and not neighbors.split():
                print("Danh sách đỉnh kề không hợp lệ. Vui lòng nhập lại.")
                neighbors = input("Nhập danh sách đỉnh kề, phân tách bằng dấu cách (nếu không có, hãy nhập dấu gạch ngang '-'): ")
            if neighbors != '-':
                neighbors = neighbors.split()
            else:
                neighbors = []
            graph.add_vertex(vertex, neighbors)

    while True:
        search_choice = input("Chọn lựa chọn tìm kiếm:\n1. DFS\n2. BFS\n")
        while search_choice not in ['1', '2']:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
            search_choice = input("Chọn lựa chọn tìm kiếm:\n1. DFS\n2. BFS\n")
        
        start_vertex = input("Nhập đỉnh xuất phát: ")
        target_vertex = input("Nhập đỉnh đích: ")

        if search_choice == '1':
            dfs_graph = DFS_Graph()
            dfs_graph.graph = graph.graph.copy()
            if start_vertex in graph.graph.keys() and target_vertex in graph.graph.keys():
                if dfs_graph.dfs_search(start_vertex, target_vertex):
                    print("Đỉnh", target_vertex, "có thể được tìm thấy từ đỉnh", start_vertex, "bằng DFS.")
                else:
                    print("Đỉnh", target_vertex, "không thể được tìm thấy từ đỉnh", start_vertex, "bằng DFS.")
            else:
                print("Đỉnh xuất phát hoặc đỉnh đích không tồn tại trong đồ thị.")
        elif search_choice == '2':
            bfs_graph = BFS_Graph()
            bfs_graph.graph = graph.graph.copy()
            if start_vertex in graph.graph and target_vertex in graph.graph:
                if bfs_graph.bfs_search(start_vertex, target_vertex):
                    print("Đỉnh", target_vertex, "có thể được tìm thấy từ đỉnh", start_vertex, "bằng BFS.")
                else:
                    print("Đỉnh", target_vertex, "không thể được tìm thấy từ đỉnh", start_vertex, "bằng BFS.")
            else:
                print("Đỉnh xuất phát hoặc đỉnh đích không tồn tại trong đồ thị.")
        
        choice = input("Lựa chọn của bạn:\n1. Tiếp tục tìm kiếm\n2. Thoát\n")
        while choice not in ['1', '2']:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
            choice = input("Lựa chọn của bạn:\n1. Tiếp tục tìm kiếm\n2. Thoát\n")
        if choice == '2':
            break