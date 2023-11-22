#include <stdio.h>
#include <stdlib.h>

// Определение структуры для элемента списка
struct list {
    int field;
    struct list* next;
};

int main() {
    // Создание первого элемента списка и инициализация его значений
    struct list* l1 = (struct list*)malloc(sizeof(struct list));
    l1->field = 1;
    l1->next = NULL; // Устанавливаем указатель на следующий элемент как NULL для обозначения конца списка

    // Создание второго элемента списка и инициализация его значений и так далее...
    struct list* current = l1; // Используем временную переменную для отслеживания текущего элемента списка

    for (int i = 2; i < 101; i++) {
        current->next = (struct list*)malloc(sizeof(struct list));
        current = current->next; // Переходим к следующему элементу
        current->field = i;
        current->next = NULL; // Устанавливаем указатель на следующий элемент как NULL для конца списка
    }

    // Теперь l1 указывает на первый элемент списка, и каждый элемент имеет указатель на следующий элемент.

    // Ваш код дальше...
    current = l1;
    while (current) {
        printf("%d ", current->field);
        current = current->next;
    }
    
    // Освобождаем память, когда она больше не нужна
    current = l1;
    while (current != NULL) {
        struct list* next = current->next;
        free(current);
        current = next;
    }

    return 0;
}

// gcc -std=c99 outputfile sourcefile.c
