import qrcode

class QR_Gen:
    def __init__(self, size:int, padding:int):
        self.qrcode = qrcode.QRCode(box_size=size, border=padding)

    def creat_qr(self, f_name:str, fg:str, bg:str):
        user_input = input("Please enter your text/link: ")

        try:
            self.qrcode.add_data(user_input)
            qr_image = self.qrcode.make_image(fill_color=fg, back_color=bg)
            qr_image.save(f_name)
            print(f"Successfull created ({f_name})")

        except Exception as e:
            print(f"Error: {e}")



def main():
    myqr = QR_Gen(size=30, padding=2)
    myqr.creat_qr("sample.png", 
                fg='green', 
                bg='pink')


if __name__=="__main__":
    main()