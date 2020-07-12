class Graph:
    def __init__(self):
        self.nodes_count = -1
        self.connectivity_matrix = []
        self.nodes_colors = {}

    def read_field(self):
        with open('in.txt') as input_file:
            self.nodes_count = int(input_file.readline())
            for row in range(self.nodes_count):
                self.connectivity_matrix.append([])
                line = input_file.readline().split()
                for element in line:
                    self.connectivity_matrix[row].append(int(element))

    def find_way(self):
        queue = [(0, 1)]
        while len(queue) != 0:
            node = queue.pop()
            self.nodes_colors[node[0]] = node[1]
            for neighbour in range(self.nodes_count):
                if self.connectivity_matrix[node[0]][neighbour] == 0:
                    continue
                if neighbour not in self.nodes_colors:
                    queue.append((neighbour, 3 - node[1]))
                elif self.nodes_colors[node[0]] == self.nodes_colors[neighbour]:
                    return False
        return True

    def get_coloring(self):
        with open('out.txt', 'w') as output_file:
            if self.find_way():
                output_file.write('Y\n')
                first_color = []
                second_color = []
                for key in self.nodes_colors:
                    if self.nodes_colors[key] == 1:
                        first_color.append(key)
                    else:
                        second_color.append(key)
                first_color.sort(reverse=True)
                second_color.sort(reverse=True)
                while len(first_color) != 0:
                    output_file.write(f'{first_color.pop() + 1} ')
                output_file.write('\n0\n')
                while len(second_color) != 0:
                    output_file.write(f'{second_color.pop() + 1} ')
            else:
                output_file.write('N')


def main():
    graph = Graph()
    graph.read_field()
    graph.get_coloring()
    print('Complete')


if __name__ == '__main__':
    main()
