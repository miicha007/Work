import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from CreatGraphic import Graph_for_plt

class plt_and__canavas_animation(FuncAnimation,FigureCanvas):
    def __init__(self):
        self.s = Graph_for_plt()
        self.fig, (self.ax1, self.ax2) = plt.subplots(nrows=2,dpi=60)
        self.ax1.set_xlabel(' время (с)    ',
                      fontsize=15)
        self.ax1.grid()
        self.ax2.grid()

        self.ax2.set_xlabel('отклонение',fontsize=15)
        self.ax2.set_ylabel('скорость',fontsize=15)
        self.ax1.set_ylim(-700, 700)
        self.ax1.set_xlim(0, 600)
        self.ax2.set_xlim(-75, 75)
        self.ax2.set_ylim(-45, 45)
        self.plot_instance, = self.ax1.plot([], lw=2)
        self.plot_instance2, = self.ax1.plot([], lw=2)
        self.plot_instance3, = self.ax2.plot([], lw=2)
        self.plot_instance4, = self.ax1.plot([], lw=2)
        self.t, self.x0, self.y0, self.xP ,self.FshP= self.s.set_data()
        self.Canavas = FigureCanvas.__init__(self, self.fig)
        self.ani = FuncAnimation.__init__(self, self.fig, self.animation_for_plt, init_func=self.init_plot, frames=1,
                               interval=5, )
        self.pause = True

    def reset_mas_for_plot(self):
        self.t, self.x0, self.y0, self.xP, self.FshP = self.s.set_data()
    def animation_for_plt(self,i):

        if not self.pause:
            self.s.Ras1()
            self.plot_instance.set_data(self.t, self.x0)
            self.plot_instance2.set_data(self.t, self.y0)
            self.plot_instance4.set_data(self.t[:-1], self.FshP)
            self.plot_instance3.set_data(self.x0[:-1],self.xP)
        return
    def init_plot(self):
        if not self.pause:
            self.plot_instance.set_data([],[])
            self.plot_instance2.set_data([], [])
            self.plot_instance3.set_data([], [])
            self.plot_instance4.set_data([], [])
    def getFig(self):
        return self.fig
    def start(self,event):
        self.pause ^= True





