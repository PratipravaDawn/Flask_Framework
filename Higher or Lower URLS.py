from flask import Flask
import random as r

num_gif = "https://media.giphy.com/media/IsfrRWvbUdRny/giphy.gif?cid=790b76110xkmeayxfcmtlhwvh77ww8zuiqpycu6jx7oau8sm&ep=v1_gifs_search&rid=giphy.gif&ct=g"
happy = "https://media.giphy.com/media/bt8FwKXiNKRkQ/giphy.gif?cid=790b7611om5692u1x2fngdn3v7lxwhlbd1rbbaht4a0fj9a2&ep=v1_gifs_search&rid=giphy.gif&ct=g"
high_gif = "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExazhwY3RxMjRuanRpcmVyZXA4YzlhcnlhZWM1OXd0dm9oMGJ2anRjdiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/bcqAMUTUHoLDy/giphy.gif"
low_gif = "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExYXc2bHRiYzJkaWYyZDJibDdwZ3l3ZnB0YWx2bGkwbm16dnY0aTZkOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3OhXBaoR1tVPW/giphy.gif"

app = Flask(__name__)
i = r.randint(0, 9)

right = ('<h1 style="color:green;">You got it right</h1>'
         f'<img src={happy} width="400" alt="happy cat">')

high = ('<h1 style="color:purple;">Too High, Try again</h1>'
        f'<img src={high_gif} width="400" alt="angry cat with gun">')

low = ('<h1 style="color:red;">Too Low, Try again </h1>'
       f'<img src={low_gif} width="400" alt="depressed cat">')

page = ('<h1>Guess a number between 0 to 9</h1>'
        f'<img src={num_gif} width="400" alt="numbers 0 to 9">')


@app.route('/')
def local():
    return page


@app.route('/<int:n>')
def guess(n):
    if n > i:
        return high
    if n < i:
        return low
    else:
        return right


if __name__ == "__main__":
    app.run(debug=True)
