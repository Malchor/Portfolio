from tkinter import Tk, Toplevel, Label, Button, Entry, Frame, Text, OptionMenu, StringVar
from UoP_wk13_questions_backend import Task, TaskList
from UoP_wk13_questions_backend import Recipe, RecipeBook
from UoP_wk13_questions_backend import Laptop, GamingLaptop, ShoppingCart


class TaskApp:
    def __init__(self, root):
        self.root = root
        root.title("Task List")
        root.geometry("400x300")

        self.task_list = TaskList()

        Label(root, text="New Task:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.new_task_entry = Entry(root, width=40)
        self.new_task_entry.grid(row=0, column=1, padx=5, pady=5)
        Button(root, text="Add Task", command=self.add_task).grid(row=0, column=2, padx=5, pady=5)

        self.task_frame = Frame(root)
        self.task_frame.grid(row=1, column=0, columnspan=3, padx=5, pady=10, sticky="w")

        self.show_tasks()

    def add_task(self):
        message = self.new_task_entry.get()
        if message != "":
            self.task_list.create_new_task(message)
            self.new_task_entry.delete(0, len(self.new_task_entry.get()))
            self.show_tasks()

    def show_tasks(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        for i in range(self.task_list.get_num_tasks()):
            task_message = self.task_list.get_task_message_by_index(i)
            Label(self.task_frame, text=task_message, width=30, anchor="w").grid(row=i, column=0, padx=5, pady=2)
            Button(self.task_frame, text="Edit", command=lambda index=i: self.edit_task(index)).grid(row=i, column=1, padx=5)
            Button(self.task_frame, text="Delete", command=lambda index=i: self.delete_task(index)).grid(row=i, column=2, padx=5)

    def delete_task(self, index):
        self.task_list.remove_task_at_index(index)
        self.show_tasks()

    def edit_task(self, index):
        task_message = self.task_list.get_task_message_by_index(index)
        popup = Toplevel(self.root)
        popup.title("Edit Task")
        popup.geometry("350x100")

        Label(popup, text="Edit Task:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        entry = Entry(popup, width=40)
        entry.grid(row=0, column=1, padx=5, pady=5)
        entry.insert(0, task_message)

        def save():
            new_message = entry.get()
            if new_message != "":
                self.task_list.set_task_message_at_index(index, new_message)
                self.show_tasks()
                popup.destroy()

        Button(popup, text="Save", command=save).grid(row=1, column=0, columnspan=2, pady=5)



class RecipeBookApp:
    def __init__(self, root):
        self.root = root
        root.title("Recipe Book")
        root.geometry("220x150")

        self.book = RecipeBook()
        self.book.add(Recipe("Spaghetti","30 min",
            "1. Boil pasta\n2. Cook meat\n3. Add sauce\n4. Mix\n5. Serve"))
        self.book.add(Recipe("Pancakes","20 min",
            "1. Mix\n2. Heat pan\n3. Pour\n4. Flip\n5. Serve"))

        i = 0
        for r in self.book.get_all():
            Label(root, text=r.get_name()).grid(row=i, column=0, padx=2, pady=2)
            Label(root, text=r.get_time()).grid(row=i, column=1)
            Button(root, text="View",
                   command=lambda x=r: self.open(x))\
                .grid(row=i, column=2, padx=2)
            i += 1

    def open(self, r):
        w = Toplevel(self.root)
        w.title(r.get_name())
        w.geometry("350x230")

        Label(w, text=r.get_name()).grid(row=0, column=0)
        Label(w, text="Time: " + r.get_time()).grid(row=1, column=0)

        t = Text(w, height=8, width=35)
        t.grid(row=2, column=0)
        t.insert("1.0", r.get_steps())
        t.config(state="disabled")



class LaptopShopApp:
    def __init__(self, root):
        self.root = root
        root.title("Laptop Shop")
        root.geometry("200x100")

        self.cart = ShoppingCart()

        Button(root, text="Add Laptop",
               command=self.add_window).grid(row=0, column=0, pady=2)

        self.frame = Frame(root)
        self.frame.grid(row=1, column=0)

        self.total_lbl = Label(root, text="Total: $0")
        self.total_lbl.grid(row=2, column=0)

        self.update()

    def update(self):
        for w in self.frame.winfo_children():
            w.destroy()

        i = 0
        for l in self.cart.get_all():
            Label(self.frame, text=str(l)).grid(row=i, column=0)
            Button(self.frame, text="Remove",command=lambda x=l: self.remove(x)).grid(row=i, column=1)
            i += 1

        self.total_lbl.config(text="Total: $" + str(self.cart.total()))

    def remove(self, l):
        self.cart.remove(l)
        self.update()

    def add_window(self):
        w = Toplevel(self.root)
        w.title("Add")
        w.geometry("250x200")

        Label(w, text="Brand").grid(row=0, column=0)
        b = Entry(w)
        b.grid(row=0, column=1)

        Label(w, text="Price").grid(row=1, column=0)
        p = Entry(w)
        p.grid(row=1, column=1)

        Label(w, text="RAM").grid(row=2, column=0)
        r = Entry(w)
        r.grid(row=2, column=1)

        Label(w, text="Type").grid(row=3, column=0)
        tvar = StringVar(w)
        tvar.set("Normal")
        OptionMenu(w, tvar, "Normal", "Gaming").grid(row=3, column=1)

        Label(w, text="GPU").grid(row=4, column=0)
        g = Entry(w)
        g.grid(row=4, column=1)

        def add():
            if tvar.get() == "Gaming":
                l = GamingLaptop(b.get(), float(p.get()),int(r.get()), g.get())
            else:
                l = Laptop(b.get(), float(p.get()), int(r.get()))
            self.cart.add(l)
            self.update()
            w.destroy()

        Button(w, text="Add", command=add).grid(row=5, column=0, columnspan=2, pady=2)


class MainApp:
    def __init__(self, root):
        self.root = root
        root.title("Main Menu")
        root.geometry("200x150")

        Button(root, text="Recipe Book", command=self.open_recipe_book)\
            .pack(pady=10)
        Button(root, text="Laptop Shop", command=self.open_laptop_shop)\
            .pack(pady=10)
        Button(root, text="Task List", command=self.open_task_list)\
            .pack(pady=10)

    def open_recipe_book(self):
        w = Toplevel(self.root)
        RecipeBookApp(w)

    def open_laptop_shop(self):
        w = Toplevel(self.root)
        LaptopShopApp(w)
        
    def open_task_list(self):
        w = Toplevel(self.root)
        TaskApp(w)
        
if __name__ == "__main__":
    root = Tk()
    MainApp(root)
    root.mainloop()
    
