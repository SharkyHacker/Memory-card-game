#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle, randint
#Скрываем группу вопросов показываем группу резултатов
class Question():
    def __init__(self, question_text, fine_answr, bad1, bad2, bad3):
        self.question_text=question_text
        self.fine_answr=fine_answr
        self.bad1=bad1
        self.bad2=bad2
        self.bad3=bad3
def show_Question():
    result_box.hide()
    answer_group.show()
    button.setText('Отвечай!')

def asK(q:Question):
    shuffle(answers)
    answers[0].setText(q.fine_answr)
    answers[1].setText(q.bad1)
    answers[2].setText(q.bad2)
    answers[3].setText(q.bad3)
    question.setText(q.question_text)
    right_answer.setText(q.fine_answr)
    show_Question()
def show_result():
    answer_group.hide()
    result_box.show()
    button.setText("Вперёд к другому вопросу")

def start_programm():
    if button.text() == ('Отвечай!'):
        show_result()
    else:
        show_Question()
def check_answr():
    if answers[0].isChecked():
        result_text.setText("Правильно, Молодец!")
        show_result()
        main_win.score =+1
    else:
        result_text.setText('НЕ правильно, попробуй ещё раз!')
        show_result()
    print('Вопросов было:', main_win.total)
    print('Вот твой счёт:', main_win.score)
    print('Твой Рейтинг:', main_win.score/total *100)
    print('За наши услуги вы должны заплатить нам: 83447243897249738289$')
#Subscribe for show_result he is good
def Next_question():
    main_win.total += 1
    cur_question = randint(0, len(questionlist)-1)
    q=questionlist[cur_question]
    asK(q)
def click_Alright():
    if button.text() == 'Отвечай!':
        check_answr()
    else:
        Next_question()
app = QApplication([])
main_win = QWidget()
question = QLabel("Что такое солёный огурец?")
button = QPushButton('Отвечай!')
answer_group = QGroupBox("Варианты ответов")
#привязываем главные направляющие(вопрос, 2 группы)
vline = QVBoxLayout()

main_win.setLayout(vline)
main_win.total = 0
main_win.score = 0
total =+1
main_win.resize(400,300)
main_win.setWindowTitle('Memory Card')
answer1 = QRadioButton('135000')
answer2 = QRadioButton('Олень')
answer3 = QRadioButton('Он ел кашу')
answer4 = QRadioButton('vline.addWidget(button)')
answers = [answer1, answer2, answer3, answer4]
v1 = QVBoxLayout()
v1.addWidget(answer1)
v1.addWidget(answer2)
v2 = QVBoxLayout()
v2.addWidget(answer3)
v2.addWidget(answer4)
h = QHBoxLayout()
h.addLayout(v1)
h.addLayout(v2)
answer_group.setLayout(h)
result_box = QGroupBox("Результат")
result_text = QLabel('Правильно - НЕправильно')
right_answer = QLabel('Верный ответ')
v3 = QVBoxLayout()
v3.addWidget(result_text)
v3.addWidget(right_answer)
#Hide group with answers
#answer_group.hide()
result_box.setLayout(v3)
vline.addWidget(question, alignment = Qt.AlignCenter)
vline.addWidget(answer_group)
vline.addWidget(result_box)
vline.addWidget(button)
question1=Question('Что такое Лось?', "Олень👌", "Охрана Здоровья👌", "Виндовс👌", "Сатиры🎃")
question2=Question("Что такое солёный огурец?", '135000', 'Олень', 'Он ел кашу', 'vline.addWidgetbutton')
question3=Question('Как называют жителей города Гусь-Хрустальный?', 'Гусевчане', 'Гусетяне', 'Гусятцы', 'Гусовцы')
question4=Question('В какой АУ андертейла санс носит большую кисть за спиной?', 'Inktale', 'Underswap', 'Errortale', 'Underfresh')
question5=Question('Как с испанского переводится Yo cocino una manzana?', 'Я готовлю яблоко', 'Я пью воду', 'Ты готовишь яблоко', 'Ты пьёшь воду')
question6=Question('Как звали троих главных героев из Deltarune?', "Крис, Ральзей, Сьюзи", "Спамтон, Майк, Зак", "Молчун, тёмный принц, динозавр-вандал", "Санс, фриск, маффет")
question7=Question("Монооксид дигидрогена что это?", 'Вода', 'Кислота', 'Вид пластика', 'Ядовитый газ')
question8=Question('Самая опасная кислота', 'Гексафтороантимонат водорода', 'Серная кислота', 'Магическая кислота', 'Царская водка')
question9=Question('Какой йолосвейнер приходит 20 декабря', 'Колбасовхат', 'Горшколиз', 'Свечной попрошайка', 'Дверехлоп')
question10=Question('Кто проживает на дне океана?', 'Спанчбоб Скверпентс!', 'Селёдка Подшубкой!', 'Булка Счаем!', 'Крот Кубокрот!')
question11=Question('Финальный босс в 16 концовке The binding of Isaac', 'Мега Сатана', 'Мама','Сатана', 'Айзек')
button.clicked.connect(click_Alright)

questionlist=[question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11]
main_win.curquestion=-1
Next_question()
main_win.show()
app.exec_()
