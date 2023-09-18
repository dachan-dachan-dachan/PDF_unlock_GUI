import os
import tkinter as tk
import tkinter.filedialog
from pikepdf import Pdf


class TkinterClass:

    def __init__(self):
        root = tk.Tk()
        root.geometry("500x350")

        button = tk.Button(root, text='パスワードを解除したいpdfを選択', font=('', 20), width=27, height=1, bg='#999999', activebackground="#aaaaaa")
        button.bind('<ButtonPress>', self.file_dialog)
        button.pack(pady=40)

        self.file_name = tk.StringVar()
        self.file_name.set('未選択です')
        label = tk.Label(textvariable=self.file_name, font=('', 12))
        label.pack(pady=0)

        password_entry = tk.Entry(root)
        password_entry.pack(pady = 20)

        label2 = tk.Label(root, text = "パスワードを入力してください")
        label2.pack()

        def go():
            locked_filename = self.file_name.get()
            if locked_filename != "未選択です":
                pas = password_entry.get()
                try:
                    pdf = Pdf.open(locked_filename, password=pas)
                    pdf_unlock = Pdf.new()
                    pdf_unlock.pages.extend(pdf.pages)
                    newfilename = locked_filename[:len(locked_filename) - 4] + "_unlock.pdf"
                    if os.path.exists(newfilename):
                        i = 1
                        newfilename = locked_filename[:len(locked_filename) - 4] + f"_unlock({i}).pdf"
                        while os.path.exists(newfilename):
                            i += 1
                            newfilename = locked_filename[:len(locked_filename) - 4] + f"_unlock({i}).pdf"
                    pdf_unlock.save(newfilename)
                    x = newfilename.rfind('/')
                    only_name = newfilename[(x+1):]
                    label3 = tk.Label(root, text = f"{only_name}で保存が完了しました")
                    label3.pack()
                except:
                    label3 = tk.Label(root, text = "パスワードが間違っている可能性があります")
                    label3.pack()
            else:
                label3 = tk.Label(root, text = "パスワードを解除したいpdfファイルを選択してください")
                label3.pack()


        button2 = tk.Button(root, text = "実行", command = go)
        button2.pack()

        root.mainloop()

    def file_dialog(self, event):
        fTyp = [("", "*.pdf")]
        iDir = os.path.abspath(os.path.dirname(__file__))
        file_name = tk.filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)
        if len(file_name) == 0:
            self.file_name.set('選択をキャンセルしました')
        else:
            self.file_name.set(file_name)


if __name__ == '__main__':
    TkinterClass()
