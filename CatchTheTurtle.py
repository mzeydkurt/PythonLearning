import turtle
import random
#Ekranı oluşturup yapılandırıyoruz.
drawing_board = turtle.Screen()  #Ekranımızı tanımlıyoruz
drawing_board.bgcolor("light blue") #Ekranımızın arka plan rengini seçiyoruz
drawing_board.title("CatchTheTurtle") #Başlığımızı yazıyoruz
drawing_board.setup(800,800) #Ekranın boyutunu ayarlıyoruz.

#Turtle ı oluşturuyoruz.
catchturtle = turtle.Turtle()
catchturtle.color("green")#Rengini belirliyoruz.
catchturtle.shape("turtle")#Şeklini belirliyoruz
catchturtle.penup()#Turtle ın iz bırakmasını engelliyoruz
#Skoru için ayrı bir Turtle tanımlıyoruz
score_pen = turtle.Turtle()
score_pen.hideturtle()#Turtle ı gizliyoruz
score_pen.penup()#Turtle ın iz bırakmasını engelliyoruz
score_pen.goto(-40,370)# Belirtilen koordinatlara gönderiyoruz
score_pen.write("Score :  ", align="left", font=("Arial", 16, "normal")) #ilk baştaki score yazısını yazdırıyoruz.

#Sayac göstergesi için Turtle oluşturuyoruz.
counter_pen = turtle.Turtle()
counter_pen.hideturtle()#Turtle ı gizliyoruz
counter_pen.penup()#Turtle ın iz bırakmasını engelliyoruz
counter_pen.goto(-40,350)# Belirtilen koordinatlara gönderiyoruz
#score_pen.write("Time :  ", align="left", font=("Arial", 16, "normal"))

score = 0 #Başlangıçtaki Skor
time_left = 20 #Başlangıçtaki Zaman
# Kaplumbağayı rastgele bir pozisyona taşır ve belirli bir süre sonra tekrar çağırmak için bir fonksiyon oluşturuyoruz.
def random_turtle():
    if time_left > 0:
        x = random.randint(-390,330) #x koordinatını rastgele belirle
        y = random.randint(-390,330) #y koordinatını rastgele belirle
        catchturtle.hideturtle()#Turtle ı gizliyoruz
        catchturtle.goto(x,y)# Belirtilen koordinatlara gönderiyoruz
        catchturtle.showturtle()#Turtle ı gösteriyoruz
        drawing_board.ontimer(random_turtle,1500) #1,5 saniyede bir göstermesini sağlıyoruz
#Kaplumbağa tıklandığında skorun güncellenmesi için ayrı bir fonksiyon oluşturuyoruz.
def update_score(x,y):
    global score #üstte tanımladığımız score global olarak alıp bu fonk da kullanıyoruz
    score += 1 #her tıklandıpında skoru +1 arttırıyoruz
    score_pen.clear()  # skor yazısını temizliyoruz
    score_pen.write(f"Score :{score}", align="left", font=("Arial", 16, "normal")) # yeni skoru ekrana yazdırıyoruz.
#Gerisayım fonksiyonu oluşturuyoruz.
def countdown():
    global time_left #üstte tanımladığımız time_left i global olarak alıp bu fonk da kullanıyoruz
    if time_left>0:
        time_left-=1 #süreyi bir azalt
        counter_pen.clear() #temizliyor
        counter_pen.write(f"Time : {time_left}", align="left", font=("Arial", 16, "normal")) #kalan süreyi ekrana yazdırır
        drawing_board.ontimer(countdown,1000)# 1000 milisaniye (1 saniye) sonra countdown() fonksiyonunu tekrar çağır
    else:
        catchturtle.hideturtle() # Süre bitince kaplumbağayı gizle
        counter_pen.goto(0,0) # Yazı kalemini ortalayacak şekilde konumlandır
        counter_pen.write("Game Over!", align="center", font=("Arial", 24, "normal"))# game over yazsını yazdırır.

catchturtle.onclick(update_score)# Kaplumbağaya tıklanma olayını update_score() fonksiyonuna bağla
countdown()# Geri sayımı başlat
random_turtle() # Kaplumbağayı rastgele pozisyona taşı ve hareket ettir

turtle.mainloop()
