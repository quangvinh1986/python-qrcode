# 5 Phút Làm Quen với QRCode Bằng Python ?

Bạn muốn gửi một thông điệp nhanh chóng cho người khác bằng một QRCode, hãy để Python giúp bạn, chỉ 5' thôi.

Trong những năm gần đây, đi đâu chúng ta cũng gặp các ô vuông với các hoa văn loằng ngoằng ở trên mà từ ngữ kỹ thuật người ta là QR-Code. QR-Code là gì? Và tạo ra nó như thế nào ? 

Chỉ bằng vài lần gõ tạch tạch trên google là chúng ta sẽ biết QR-Code là gì và lợi ích của nó mang lại cho mọi người trong đời sống như thế nào. Vì thế bài viết của tôi không muốn đưa lại nhiều những thông tin mà đã có quá nhiều trên internet nữa (Các bạn tự tìm kiếm nhé).

QR-Code, viết tắt của Quick response code (tạm dịch "Mã phản hồi nhanh") hay còn gọi là mã vạch ma trận (matrix-barcode) là dạng mã vạch hai chiều (2D) có thể được đọc bởi một máy đọc mã vạch hay smartphone (điện thoại thông minh) có chức năng chụp ảnh (camera) với ứng dụng chuyên biệt để quét mã vạch. (https://vi.wikipedia.org/wiki/M%C3%A3_QR)

Có nhiều công cụ để sinh ra các "ô vuông" chứa mã QRCode, dưới đây là cách dùng code Python để sinh ra một mã QR-Code.
1. Cài đặt thư viện.
Để bắt đầu cài đặt thư viện, chúng ta sẽ tạo ra một virtual environment nhé, hướng dẫn có thể xem tại đây Làm Chủ Python Virtual Environment - Môi Trường Lập Trình Ảo ?
 https://codelearn.io/sharing/quick-quide-python-virtual-environment

Sau khi cài đặt xong VE, chúng ta activate môi trường lên và bắt đầu install 2 thư viện: pillow, qrcode (https://pypi.org/project/qrcode/)

(qr_code_venv) E:\code_learn\QRCode>pip install pillow
Collecting pillow
  Downloading https://files.pythonhosted.org/packages/91/d2/30ecd905746d1fee4004daae3f0051bf4b305bee1fe578bd7d1ea712d571/Pillow-7.2.0-cp38-cp38-win_amd64.whl (2.1MB)
     |████████████████████████████████| 2.1MB 504kB/s
Installing collected packages: pillow
Successfully installed pillow-7.2.0

(qr_code_venv) E:\code_learn\QRCode>pip install qrcode
Collecting qrcode
  Downloading https://files.pythonhosted.org/packages/42/87/4a3a77e59ab7493d64da1f69bf1c2e899a4cf81e51b2baa855e8cc8115be/qrcode-6.1-py2.py3-none-any.whl
Collecting colorama; platform_system == "Windows" (from qrcode)
  Downloading https://files.pythonhosted.org/packages/44/98/5b86278fbbf250d239ae0ecb724f8572af1c91f4a11edf4d36a206189440/colorama-0.4.4-py2.py3-none-any.whl
Collecting six (from qrcode)
  Using cached https://files.pythonhosted.org/packages/ee/ff/48bde5c0f013094d729fe4b0316ba2a24774b3ff1c52d924a8a4cb04078a/six-1.15.0-py2.py3-none-any.whl
Installing collected packages: colorama, six, qrcode
Successfully installed colorama-0.4.4 qrcode-6.1 six-1.15.0

2. Sinh mã QRCode 

Tôi sẽ dùng đường dẫn đến danh sách các bài viết của tôi trên CodeLearn để thực hiện chuyển lên mã QR-Code: https://codelearn.io/sharing/post/Quangvinh1986


import qrcode

my_url = "https://codelearn.io/sharing/post/Quangvinh1986"

qr = qrcode.QRCode(version=1, box_size=10, border=5)


Ở đây, tôi sẽ tạo ra một mã QR với các giá trị: 
version: Nhận giá trị từ 1 đến 40; với 1 là giá trị nhỏ nhất, tương đương với ma trận 2 chiều 21x21 ô.
box_size: Số lượng pixels trong mỗi ô vuông nhỏ.
border: Độ dày đường viền của box. Mặc định là 4 - tối thiểu.


qr.add_data(my_url)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')
img.save('my_codelearn.png')

Tham số fit cho phép mã QR được phép "tràn" hết ra các bên. 
fill: Cho phép thiết lập màu của các hoa văn trên mã QR.
back_color: Cho phép thiết lập màu của background trên mã QR.

Save nội dung đoạn code trên vào file qr_code.py, sau đó đứng từ vị trí của VE đã được activate thực hiện gõ lệnh python qr_code.py
Kết quả thu được sẽ là file ảnh my_codelearn.png

(qr_code_venv) E:\code_learn\QRCode>dir
 Volume in drive E is New Volume
 Volume Serial Number is 642C-F508

 Directory of E:\code_learn\QRCode

10/13/2020  10:24 PM    <DIR>          .
10/13/2020  10:24 PM    <DIR>          ..
10/13/2020  10:24 PM               264 qr_code.py
10/13/2020  10:08 PM    <DIR>          qr_code_venv
               1 File(s)            264 bytes
               3 Dir(s)  33,125,154,816 bytes free

(qr_code_venv) E:\code_learn\QRCode>
(qr_code_venv) E:\code_learn\QRCode>
(qr_code_venv) E:\code_learn\QRCode>python qr_code.py

(qr_code_venv) E:\code_learn\QRCode>dir
 Volume in drive E is New Volume
 Volume Serial Number is 642C-F508

 Directory of E:\code_learn\QRCode

10/13/2020  10:25 PM    <DIR>          .
10/13/2020  10:25 PM    <DIR>          ..
10/13/2020  10:25 PM               775 my_codelearn.png
10/13/2020  10:24 PM               264 qr_code.py
10/13/2020  10:08 PM    <DIR>          qr_code_venv
               2 File(s)          1,039 bytes
               3 Dir(s)  33,125,150,720 bytes free

Mở file trên, chúng ta được một ảnh: 

my_codelearn.png


Thử dùng Zalo thực hiện quét mã này và thu được thông điệp: 
zalo_quet.png


3. Đọc mã QR

Để đọc mã QR, chúng ta sẽ thực hiện cài đặt thư viện: pyzbar (trước đó thì phải có thư viện pillow).

(qr_code_venv) E:\code_learn\QRCode>pip install pyzbar
Collecting pyzbar
  Downloading https://files.pythonhosted.org/packages/3d/14/97bf8e36fb58965415e3c7d8f95cfd6375cb0b5464ae9dbc0a48f7f9ab19/pyzbar-0.1.8-py2.py3-none-win_amd64.whl (813kB)
    100% |████████████████████████████████| 819kB 514kB/s
Installing collected packages: pyzbar
Successfully installed pyzbar-0.1.8


Để thực hiện "giải mã", chúng ta cần phải đọc được ảnh lên trước, chúng ta sẽ dùng thư viện PIL để thực hiện việc đọc ảnh (lưu ý là nên truyền đường dẫn tuyệt đối đến ảnh nếu như bạn không để ảnh cùng thư mục với file .py nhé).

Trong ví dụ này, chúng ta sẽ thực hiện "giải mã" 2 file: file thứ 1 là file vừa sinh phía trên, file thứ 2 là file được tạo từ một phần mềm khác có định dạng: 

qr-code.png


from PIL import Image
from pyzbar import pyzbar

img = Image.open('qr-code.png')
qr_output = pyzbar.decode(img)

print("qr-code.png decode:" )
print(qr_output)

img = Image.open('my_codelearn.png')
my_qr_output = pyzbar.decode(img)

print("my_codelearn.png decode:" )
print(my_qr_output)

Save đoạn code trên thành file read_qrcode.py và thực hiện chạy file trên virtual environment đã activate và cài đặt đủ thư viện: 

(qr_code_venv) E:\code_learn\QRCode>python read_qrcode.py
qr-code.png decode:
[Decoded(data=b'https://codelearn.io/', type='QRCODE', rect=Rect(left=67, top=67, width=1020, height=1020), polygon=[Point(x=67, y=67), Point(x=67, y=1087), Point(x=1087, y=1087), Point(x=1087, y=67)])]
my_codelearn.png decode:
[Decoded(data=b'https://codelearn.io/sharing/post/Quangvinh1986', type='QRCODE', rect=Rect(left=50, top=50, width=330, height=330), polygon=[Point(x=50, y=50), Point(x=50, y=379), Point(x=380, y=380), Point(x=379, y=50)])]

Kết quả decode mà chúng ta thu được là các đối tượng Decoded với thuộc tính data chính là nội dung của thông tin chúng ta encode lúc trước, kèm theo nó là các thuộc tính khác liên quan đến vị trí đặt các ô vuông chứa thông tin. 

Kết
Trên đây tôi đã giới thiệu với các bạn cách đọc và ghi thông tin với QR-Code. Ứng dụng của QR-Code thì rất nhiều, biết đâu một ngày nào đó chúng ta sẽ dùng đến. 
Cảm ơn các bạn đã đọc bài viết. 

