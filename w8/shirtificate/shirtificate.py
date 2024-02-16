from fpdf import FPDF, Align


class Shirtificate(FPDF):
    def __init__(self, name= 'student'):
        super().__init__(orientation='portrait', unit='mm', format='A4', font_cache_dir='DEPRECATED')
        self._name = name

    def header(self):
        self.set_font("helvetica", "B", 50)
        self.cell(30, 50, "CS50 Shirtificate", border=0, align="C", center=True)
        self.image("shirtificate.png",x = Align.C, y = 80)
        self.set_text_color(255, 255, 255)
        self.set_font("helvetica", "B", 35)
        self.cell(30, 300, f"{self._name} Took CS50", border=0, align="C", center=True)

    @classmethod
    def get(cls):
        name = input("Name: ").strip()
        return cls(name)


def main():
    pdf = Shirtificate.get()  # Uses the class method to instantiate the PDF object
    pdf.add_page()
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()

