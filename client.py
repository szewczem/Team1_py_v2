class Client:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def client_data(self):
        data = {
            "name": self.name,
            "age": self.age,
            "gender": self.gender
        }
        return data
    

class ClientsList:
    def __init__(self, filename):
        self.filename = filename
    
    def count_client(self):
        with open(self.filename, 'r') as f:
            lines = len(f.readlines())
            return lines

    def add_to_clients_list(self, new_client):
        with open(self.filename, "a") as f:       
            num_client = int(self.count_client()) + 1
            f.write(f"{num_client}  ")    
            for key, value in new_client.client_data().items():
                f.write('%s: %s  ' % (key, value))
            else:
                f.write('\n')                

    def read_clients_list(self):
        self.filename = open("clients_list.txt", "r")
        content = self.filename.read()
        print(content)
        self.filename.close()

    def load_to_list(self):
        self.filename = open("clients_list.txt", "r")
        data = self.filename.read()
        data_into_list = data.split('\n')

        last_line = len(data_into_list)-1
        del data_into_list[last_line]

        data_into_list = [item.split(" ") for item in data_into_list]

        clients_list_into_list = []
        for i in data_into_list:
            i = [j for j in i if j]
            clients_list_into_list.append(i)
        self.filename.close()
        return clients_list_into_list

    def winners_list(self):
        clients_list = self.load_to_list()
        high_age = []
        for i in clients_list:
            high_age.append(i[4])
        high_age.sort(reverse=True)

        winners_list_age = high_age[0:3]

        winner_list = []
        for i in winners_list_age:
            for j in clients_list:
                if i in j:
                    winner_list.append(j)

        winner_list_str = []
        for i in winner_list:
            i = ' '.join(i)
            winner_list_str.append(i)

        num_winner = len(winner_list_str)

        with open("winners.txt", "w") as f:
            for i in range(num_winner):
                    f.write(f"{i+1}.  {winner_list_str[i]}\n")                             

    def read_winners_list(self):
        self.winners_list()
        filename = open("winners.txt", "r")
        content = filename.read()
        print(content)
        filename.close()


# clients_list = ClientsList()
# u1 = Client("Tom",25,"M")
# u2 = Client("Bob",45,"M")
# u3 = Client("Anna",29,"F")
# u4 = Client("Edward",35,"M")
# u5 = Client("Steve",95,"M")
# u6 = Client("V",20,"F")
# u7 = Client("Nina",34,"F")
# u8 = Client("Adam",23,"M")
# u9 = Client("Katarzyna",55,"F")
# u10 = Client("Artur",65,"M")

# clients_list.add_to_clients_list(u1)
# clients_list.add_to_clients_list(u2)
# clients_list.add_to_clients_list(u3)
# clients_list.add_to_clients_list(u4)
# clients_list.add_to_clients_list(u5)
# clients_list.add_to_clients_list(u6)
# clients_list.add_to_clients_list(u7)
# clients_list.add_to_clients_list(u8)
# clients_list.add_to_clients_list(u9)
# clients_list.add_to_clients_list(u10)

# clients_list.read_clients_list()
# clients_list.read_winners_list()
