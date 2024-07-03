import tkinter as tk
from tkinter import messagebox
import random
import math

class Simulacao_Token_Ring:
    def __init__(self, master):
        self.master = master
        self.num_processes = 0
        self.current_token_holder = 0
        self.critical_section_in_use = False
        self.process_in_critical_section = None 
        self.critical_section_times = []

        self.setup_initial_screen()

    def setup_initial_screen(self):
        self.initial_frame = tk.Frame(self.master)
        self.initial_frame.pack()

        self.num_processes_label = tk.Label(self.initial_frame, text="Número de Processos:")
        self.num_processes_label.pack(side=tk.LEFT)
        
        self.num_processes_entry = tk.Entry(self.initial_frame)
        self.num_processes_entry.pack(side=tk.LEFT)

        self.start_button = tk.Button(self.initial_frame, text="Iniciar Simulação", command=self.start_simulation)
        self.start_button.pack(side=tk.LEFT)

    def start_simulation(self):
        try:
            self.num_processes = int(self.num_processes_entry.get())
            if self.num_processes <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número válido de processos.")
            return

        self.initial_frame.pack_forget()
        self.setup_simulation()

    def setup_simulation(self):
        self.critical_section_times = [random.randint(2000, 5000) for _ in range(self.num_processes)]  

        self.create_widgets()
        self.update_info_panel()

    def create_widgets(self):
        self.info_panel = tk.Label(self.master, text="", justify=tk.LEFT)
        self.info_panel.pack()

        self.canvas = tk.Canvas(self.master, width=500, height=500)
        self.canvas.pack()

        self.token_ring = []
        angle_step = 360 / self.num_processes
        radius = 200
        center_x = 250
        center_y = 250

        for i in range(self.num_processes):
            angle = i * angle_step
            x = center_x + radius * math.cos(angle * math.pi / 180)
            y = center_y + radius * math.sin(angle * math.pi / 180)
            process = self.canvas.create_oval(x-20, y-20, x+20, y+20, fill="lightblue")
            self.token_ring.append((process, x, y))
            self.canvas.create_text(x, y, text=str(i))

        self.critical_section = self.canvas.create_rectangle(center_x-50, center_y-50, center_x+50, center_y+50, fill="white")
        self.canvas.create_text(center_x, center_y, text="RC")

        self.next_button = tk.Button(self.master, text="Passar Token", command=self.pass_token)
        self.next_button.pack()

    def update_info_panel(self):
        current_process = self.current_token_holder
        critical_section_process = self.process_in_critical_section
        ack_nack = "ack" if critical_section_process is not None else "nack"
        release_ok = "ok" if not self.critical_section_in_use else ""
        request_fulfilled = "sim" if self.critical_section_in_use else "não"

        info_text = (
            f"Processo na região crítica: {critical_section_process if critical_section_process is not None else 'Nenhum'}\n"
            f"A região crítica está sendo acessada: {ack_nack}\n"
            f"A região crítica está sendo liberada: {release_ok}\n"
            f"Requisição atendida: {request_fulfilled}\n"
        )
        self.info_panel.config(text=info_text)

    def pass_token(self):
        if self.critical_section_in_use:
            messagebox.showinfo("Info", f"Processo {self.process_in_critical_section} está na região crítica e precisa liberar antes de passar o token.")
        else:
            if random.random() < 0.5:
                self.critical_section_in_use = True
                self.process_in_critical_section = self.current_token_holder
                messagebox.showinfo("Info", f"Processo {self.current_token_holder} está acessando a região crítica.")
                self.update_info_panel()
                self.animate_token_to_critical_section(self.current_token_holder)
            else:
                self.advance_token()

    def advance_token(self):
        self.current_token_holder = (self.current_token_holder + 1) % self.num_processes
        self.update_info_panel()
        self.canvas.itemconfig(self.token_ring[self.current_token_holder][0], fill="yellow")
        self.master.after(1000, self.reset_token_color, self.current_token_holder)

    def reset_token_color(self, process):
        self.canvas.itemconfig(self.token_ring[process][0], fill="lightblue")

    def animate_token_to_critical_section(self, process):
        x0, y0 = self.token_ring[process][1], self.token_ring[process][2]
        x1, y1 = 250, 250
        steps = 20
        dx = (x1 - x0) / steps
        dy = (y1 - y0) / steps
        self.animate_token(x0, y0, dx, dy, steps, lambda: self.keep_in_critical_section(process))

    def keep_in_critical_section(self, process):
        self.master.after(self.critical_section_times[process], self.release_critical_section)

    def release_critical_section(self):
        self.critical_section_in_use = False
        self.process_in_critical_section = None
        self.update_info_panel()
        self.animate_token_to_process(self.current_token_holder)

    def animate_token_to_process(self, process):
        x0, y0 = 250, 250
        x1, y1 = self.token_ring[process][1], self.token_ring[process][2]
        steps = 20
        dx = (x1 - x0) / steps
        dy = (y1 - y0) / steps
        self.animate_token(x0, y0, dx, dy, steps, self.advance_token)

    def animate_token(self, x0, y0, dx, dy, steps, callback):
        token = self.canvas.create_oval(x0-10, y0-10, x0+10, y0+10, fill="yellow")
        def animate_step(step):
            if step < steps:
                self.canvas.move(token, dx, dy)
                self.master.after(50, animate_step, step + 1)
            else:
                self.canvas.delete(token)
                callback()
        animate_step(0)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Simulação de Exclusão Mútua baseado em Token Ring")

    app = Simulacao_Token_Ring(root)

    root.mainloop()
