# Homework 1. ToDo List Application
# =============================
# 1️ Define Task Class
# =============================
class Task:
    def __init__(self, title, description, due_date, status="Bajarilmagan"):
        self.title = title              # Vazifa nomi
        self.description = description  # Tavsif
        self.due_date = due_date        # Muddati
        self.status = status            # Holati

    def mark_complete(self):
        """Vazifani bajarilgan deb belgilaydi"""
        self.status = "Bajarilgan"

    def display_info(self):
        """Vazifa ma'lumotlarini ekranga chiqaradi"""
        print(f"Vazifa nomi: {self.title}")
        print(f"Tavsif: {self.description}")
        print(f"Muddati: {self.due_date}")
        print(f"Holati: {self.status}")
        print("-" * 30)


# =============================
# 2️ Define ToDoList Class
# =============================
class ToDoList:
    def __init__(self):
        self.tasks = []  # Barcha Task obyektlarini saqlash

    def add_task(self, task):
        """Yangi vazifa qo‘shish"""
        self.tasks.append(task)
        print(f"'{task.title}' vazifasi ro‘yxatga qo‘shildi.")

    def mark_task_complete(self, title):
        """Vazifa nomi orqali uni bajarilgan deb belgilash"""
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                print(f"'{title}' bajarilgan deb belgilandi.")
                return
        print(f"'{title}' nomli vazifa topilmadi.")

    def list_all_tasks(self):
        """Barcha vazifalarni chiqarish"""
        if not self.tasks:
            print("Hozircha vazifalar yo‘q.")
            return
        print("\nBarcha vazifalar:")
        for task in self.tasks:
            task.display_info()

    def show_incomplete_tasks(self):
        """Faqat bajarilmagan vazifalarni ko‘rsatish"""
        incomplete_tasks = [t for t in self.tasks if t.status != "Bajarilgan"]
        if not incomplete_tasks:
            print("Barcha vazifalar bajarilgan!")
            return
        print("\nBajarilmagan vazifalar:")
        for task in incomplete_tasks:
            task.display_info()


# =============================
# 3️ Create Main CLI Program
# =============================
def main():
    todo = ToDoList()

    while True:
        print("\n=== ToDoList Dasturi ===")
        print("1. Vazifa qo‘shish")
        print("2. Vazifani bajarilgan deb belgilash")
        print("3. Barcha vazifalarni ko‘rish")
        print("4. Faqat bajarilmagan vazifalarni ko‘rish")
        print("5. Chiqish")

        tanlov = input("Tanlang (1-5): ")

        if tanlov == "1":
            title = input("Vazifa nomi: ")
            desc = input("Tavsif: ")
            due = input("Muddati (YYYY-MM-DD): ")
            new_task = Task(title, desc, due)
            todo.add_task(new_task)

        elif tanlov == "2":
            title = input("Bajarilgan vazifa nomini kiriting: ")
            todo.mark_task_complete(title)

        elif tanlov == "3":
            todo.list_all_tasks()

        elif tanlov == "4":
            todo.show_incomplete_tasks()

        elif tanlov == "5":
            print("Dasturdan chiqildi.")
            break

        else:
            print("Noto‘g‘ri tanlov. Qaytadan urinib ko‘ring.")


# =============================
# 4️ Test the Application
# =============================
if __name__ == "__main__":
    # Dastur ishga tushadi
    main()



# Homework 2. Simple Blog System

# =======================================
# 1️⃣ Define Post Class
# =======================================
class Post:
    def __init__(self, title, content, author):
        self.title = title              # Post nomi
        self.content = content          # Post mazmuni
        self.author = author            # Post muallifi

    def display_info(self):
        """Post ma'lumotlarini chiqarish"""
        print(f"Sarlavha: {self.title}")
        print(f"Muallif: {self.author}")
        print(f"Mazmun: {self.content}")
        print("-" * 40)


# =======================================
# 2️⃣ Define Blog Class
# =======================================
class Blog:
    def __init__(self):
        self.posts = []  # Barcha postlar ro‘yxati

    def add_post(self, post):
        """Yangi post qo‘shish"""
        self.posts.append(post)
        print(f"'{post.title}' nomli post qo‘shildi.\n")

    def list_posts(self):
        """Barcha postlarni chiqarish"""
        if not self.posts:
            print("Hozircha hech qanday post yo‘q.\n")
        else:
            print("Barcha postlar:")
            for post in self.posts:
                post.display_info()

    def display_by_author(self, author):
        """Muallif bo‘yicha postlarni chiqarish"""
        found = False
        for post in self.posts:
            if post.author.lower() == author.lower():
                post.display_info()
                found = True
        if not found:
            print(f"{author} tomonidan yozilgan post topilmadi.\n")

    def edit_post(self, title, new_content):
        """Postni mazmunini tahrirlash"""
        for post in self.posts:
            if post.title.lower() == title.lower():
                post.content = new_content
                print(f"'{title}' post tahrirlandi!\n")
                return
        print("❌ Post topilmadi.\n")

    def delete_post(self, title):
        """Postni nomi bo‘yicha o‘chirish"""
        for post in self.posts:
            if post.title.lower() == title.lower():
                self.posts.remove(post)
                print(f"'{title}' post o‘chirildi!\n")
                return
        print("Bunday sarlavhali post topilmadi.\n")

    def show_latest_posts(self, count=3):
        """Eng so‘nggi n ta postni chiqarish"""
        if not self.posts:
            print("Postlar mavjud emas.\n")
            return
        print("Eng so‘nggi postlar:")
        for post in self.posts[-count:]:
            post.display_info()


# =======================================
# 3️⃣ Create Main CLI Program
# =======================================
def main():
    blog = Blog()

    while True:
        print("\n=== BLOG SYSTEM ===")
        print("1. Post qo‘shish")
        print("2. Barcha postlarni ko‘rish")
        print("3. Muallif bo‘yicha postlarni ko‘rish")
        print("4. Postni tahrirlash")
        print("5. Postni o‘chirish")
        print("6. Eng so‘nggi postlarni ko‘rish")
        print("7. Chiqish")

        tanlov = input("Tanlang (1-7): ")

        if tanlov == "1":
            title = input("Post nomi: ")
            content = input("Post mazmuni: ")
            author = input("Muallif ismi: ")
            new_post = Post(title, content, author)
            blog.add_post(new_post)

        elif tanlov == "2":
            blog.list_posts()

        elif tanlov == "3":
            author = input("Muallif ismini kiriting: ")
            blog.display_by_author(author)

        elif tanlov == "4":
            title = input("Tahrir qilinadigan post nomi: ")
            new_content = input("Yangi mazmun: ")
            blog.edit_post(title, new_content)

        elif tanlov == "5":
            title = input("O‘chiriladigan post nomi: ")
            blog.delete_post(title)

        elif tanlov == "6":
            blog.show_latest_posts()

        elif tanlov == "7":
            print("Dastur yakunlandi.")
            break

        else:
            print("Noto‘g‘ri tanlov. Qayta urinib ko‘ring.")


# =======================================
# 4️⃣ Test the Application
# =======================================
if __name__ == "__main__":
    main()

# Homework 3. Simple Banking System
# =============================
# 1️⃣ Define Account Class
# =============================

class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number   # Hisob raqami
        self.holder_name = holder_name         # Egasi ismi
        self.balance = balance                 # Balans miqdori

    def deposit(self, amount):
        """Hisobga pul qo‘shish"""
        if amount > 0:
            self.balance += amount
            print(f"{amount} so‘m hisobga qo‘shildi. Yangi balans: {self.balance} so‘m.")
        else:
            print("Kiritilgan summa noto‘g‘ri!")

    def withdraw(self, amount):
        """Hisobdan pul yechish"""
        if amount <= 0:
            print("Summani to‘g‘ri kiriting!")
        elif amount > self.balance:
            print("Yetarli mablag‘ mavjud emas! Overdraft holati.")
        else:
            self.balance -= amount
            print(f"{amount} so‘m yechildi. Yangi balans: {self.balance} so‘m.")

    def display_info(self):
        """Hisob ma’lumotlarini chiqarish"""
        print(f"Hisob raqami: {self.account_number}")
        print(f"Egasining ismi: {self.holder_name}")
        print(f"Balans: {self.balance} so‘m")
        print("-" * 30)


# =============================
# 2️⃣ Define Bank Class
# =============================

class Bank:
    def __init__(self):
        self.accounts = []  # Barcha hisoblarni saqlash

    def add_account(self, account):
        """Yangi hisob qo‘shish"""
        self.accounts.append(account)
        print(f"'{account.holder_name}' nomiga yangi hisob ochildi.")

    def find_account(self, account_number):
        """Hisob raqami orqali topish"""
        for acc in self.accounts:
            if acc.account_number == account_number:
                return acc
        return None

    def check_balance(self, account_number):
        """Balansni tekshirish"""
        acc = self.find_account(account_number)
        if acc:
            print(f"Balans: {acc.balance} so‘m")
        else:
            print("Hisob topilmadi!")

    def deposit_money(self, account_number, amount):
        """Hisobga pul qo‘shish"""
        acc = self.find_account(account_number)
        if acc:
            acc.deposit(amount)
        else:
            print("Hisob topilmadi!")

    def withdraw_money(self, account_number, amount):
        """Hisobdan pul yechish"""
        acc = self.find_account(account_number)
        if acc:
            acc.withdraw(amount)
        else:
            print("Hisob topilmadi!")

    def transfer_money(self, from_acc, to_acc, amount):
        """Pulni bir hisobdan boshqasiga o‘tkazish"""
        sender = self.find_account(from_acc)
        receiver = self.find_account(to_acc)

        if not sender or not receiver:
            print("Hisoblardan biri topilmadi!")
            return

        if sender.balance < amount:
            print("Yetarli mablag‘ mavjud emas, o‘tkazma amalga oshmadi!")
            return

        sender.withdraw(amount)
        receiver.deposit(amount)
        print(f"{amount} so‘m {sender.holder_name} dan {receiver.holder_name} ga o‘tkazildi.")

    def list_all_accounts(self):
        """Barcha hisoblarni ko‘rsatish"""
        if not self.accounts:
            print("Hozircha hech qanday hisob yo‘q.")
            return
        print("\nBarcha hisoblar:")
        for acc in self.accounts:
            acc.display_info()


# =============================
# 3️⃣ Create Main CLI Program
# =============================

def main():
    bank = Bank()

    while True:
        print("\n=== Banking System Dasturi ===")
        print("1. Yangi hisob ochish")
        print("2. Balansni tekshirish")
        print("3. Hisobga pul qo‘shish")
        print("4. Hisobdan pul yechish")
        print("5. Pul o‘tkazmasi (transfer)")
        print("6. Barcha hisoblarni ko‘rish")
        print("7. Chiqish")

        tanlov = input("Tanlang (1-7): ")

        if tanlov == "1":
            acc_num = input("Hisob raqami: ")
            name = input("Egasining ismi: ")
            start_balance = float(input("Boshlang‘ich balans (0 bo‘lishi mumkin): "))
            new_acc = Account(acc_num, name, start_balance)
            bank.add_account(new_acc)

        elif tanlov == "2":
            acc_num = input("Hisob raqamini kiriting: ")
            bank.check_balance(acc_num)

        elif tanlov == "3":
            acc_num = input("Hisob raqamini kiriting: ")
            amount = float(input("Summani kiriting: "))
            bank.deposit_money(acc_num, amount)

        elif tanlov == "4":
            acc_num = input("Hisob raqamini kiriting: ")
            amount = float(input("Yechiladigan summa: "))
            bank.withdraw_money(acc_num, amount)

        elif tanlov == "5":
            from_acc = input("Qaysi hisobdan: ")
            to_acc = input("Qaysi hisobga: ")
            amount = float(input("O‘tkaziladigan summa: "))
            bank.transfer_money(from_acc, to_acc, amount)

        elif tanlov == "6":
            bank.list_all_accounts()

        elif tanlov == "7":
            print("Dasturdan chiqildi.")
            break

        else:
            print("Noto‘g‘ri tanlov, qayta urinib ko‘ring.")


# =============================
# 4️⃣ Test the Application
# =============================

if __name__ == "__main__":
    main()

