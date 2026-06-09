from tabulate import tabulate

class User:

    data = {
        1: ["Shandy", "Basic Plan", 12, "shandy-2134"],
        2: ["Cahya", "Standard Plan", 24, "cahya-abcd"],
        3: ["Ana", "Premium Plan", 5, "ana-2f9g"],
        4: ["Bagus", "Basic Plan", 11, "bagus-9f92"]
    }

    header_benefit = ["Basic Plan", "Standard Plan", "Premium Plan", "Services"]
    table_benefit = [[True, True, True, "Bisa Stream"],
                 [True, True, True, "Bisa Download"],
                 [True, True, True, "Kualitas SD"],
                 [False, True, True, "Kualitas HD"],
                 [False, False, True, "Kualitas UHD"],
                 [1, 2, 4, "Number of Devices"],
                 ["3rd party Movie only", "Basic Plan Content + Sports", "Basic Plan + Standard Plan + PacFlix Original Series", "Jenis Konten"],
                 [120_000, 160_000, 200_000, "Harga"]]


    def __init__(self):
        self.username = None
        self.duration_plan = None
        self.current_plan = None
        self.kode_referral = None


    def login(self, username):
        self.username = username

        self.duration_plan = None
        self.current_plan = None
        self.kode_referral = None

        for value in self.data.values():
            if value[0] == username:
                self.duration_plan = value[2]
                self.current_plan = value[1]
                self.kode_referral = value[3]
                break
    

    def check_benefit (self):
        print ("PacFlix Plan List")
        print ("")
        print (tabulate(self.table_benefit, self.header_benefit))

    
    def check_plan (self):
        print (f"User {self.username} sedang berlangganan")

        if (self.current_plan in self.header_benefit [0:3]):
            if self.current_plan == "Basic Plan":
                table_data = [[row[0], row[-1]] for row in self.table_benefit]
                header = [self.header_benefit[0], self.header_benefit[-1]]

            elif self.current_plan == "Standard Plan":
                table_data = [[row[1], row[-1]] for row in self.table_benefit]
                header = [self.header_benefit[1], self.header_benefit[-1]]
            
            elif self.current_plan == "Premium Plan":
                table_data = [[row[2], row[-1]] for row in self.table_benefit]
                header = [self.header_benefit[2], self.header_benefit[-1]]

            print (tabulate(table_data,header))

        else:
            raise Exception ("Data plan tidak ada")
        
    
    def upgrade_plan(self, new_plan):
            
            try:
                idx_current_plan = self.header_benefit.index(self.current_plan)
                idx_new_plan = self.header_benefit.index(new_plan)

                if(idx_current_plan < idx_new_plan):
                    
                    if(self.duration_plan > 12):
                        total = self.table_benefit[-1][idx_new_plan] - (0.05*self.table_benefit[-1][idx_new_plan])

                    else:
                        total = self.table_benefit[-1][idx_new_plan] 
                    
                    # update informasi current_plan
                    self.current_plan = new_plan
                    for key,value in self.data.items():
                        if value[0] == self.username:
                            self.data[key][1] = new_plan
                            break

                    print(f"Harga yang harus dibayarkan untuk upgrade ke {new_plan} adalah Rp.{total}")         
                
                elif(idx_current_plan == idx_new_plan):
                    print(f"Anda sedang berlangganan plan {self.current_plan}, jadi tidak bisa upgrade")

                else:
                    print("Anda tidak bisa melakukan downgrade")

            except Exception as e:
                print(str(e))        
    

    def subscribe_plan(self,plan,kode_referal):
            
            self.curent_plan = plan
            self.kode_referal = f"{self.username.lower()}-123"
            self.duration_plan = 1

            list_referal = [row[-1] for row in self.data.values()]
            idx_plan = self.header_benefit.index(plan)
            if(kode_referal in list_referal):
                #mendapatkan diskon
                total = self.table_benefit[-1][idx_plan] - (0.04*self.table_benefit[-1][idx_plan])
            else:
                total = self.table_benefit[-1][idx_plan]

            last_key = max(self.data.keys())
            self.data[last_key+1] = [self.username, self.curent_plan, self.duration_plan, self.kode_referal]

            print(f"Harga yang harus dibayarkan dari {plan} adalah Rp.{total}")
    
    

            


            
            



