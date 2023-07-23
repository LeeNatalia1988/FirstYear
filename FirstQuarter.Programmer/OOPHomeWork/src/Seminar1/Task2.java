package Seminar1;
/*
* Реализуйте класс "Прямоугольник" (Rectangle), который имеет свойства ширина (width) и высота (height). Класс должен обладать следующими методами:

Конструктор без параметров, который создает прямоугольник с шириной и высотой по умолчанию.
Конструктор, который принимает значения ширины и высоты и создает прямоугольник с заданными значениями.
Методы доступа (геттеры и сеттеры) для свойств ширины и высоты.
Метод "вычислить площадь" (calculateArea), который возвращает площадь прямоугольника (ширина * высота).
Метод "вычислить периметр" (calculatePerimeter), который возвращает периметр прямоугольника
* (2 * (ширина + высота)).*/
public class Task2 {
    public static void main(String[] args) {
        Rectangle rec_1 = new Rectangle();
        System.out.println("Площадь первого прямоугольника(по умолчанию): " + rec_1.calculateArea());
        System.out.println("Периметр первого прямоугольника(по умолчанию): " + rec_1.calculatePerimeter());
        Rectangle rec_2 = new Rectangle(5.0, 5.0);
        System.out.println("Площадь второго прямоугольника: " + rec_2.calculateArea());
        System.out.println("Периметр второго прямоугольника: " + rec_2.calculatePerimeter());
    }

}
