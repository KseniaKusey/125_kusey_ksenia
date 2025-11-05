import java.util.Scanner;

public class Main {
    private static TodoList todoList = new TodoList();

    public static void main(String[] args) {
        // TODO: написать консольное приложение для работы со списком дел todoList
        Scanner in = new Scanner(System.in);
        System.out.println(
                "Введите команды: LIST, " +
                        "ADD <задача>, " +
                        "EDIT <номер> <новая задача>, " +
                        "DELETE <номер>, " +
                        "EXIT для выхода.");

        while (true) {
            String input = in.nextLine();
            if(input == null || input.isBlank()) {
                continue;
            }

            String[] command = input.split(" ", 2);

            switch (command[0].toUpperCase()) {
                case "LIST" -> {
                    for (int i = 0; i < todoList.getTodos().size(); i++) {
                        System.out.println((i + 1) + ". " + todoList.getTodos().get(i));
                    }
                }
                case "ADD" -> {
                    if (command.length < 2 || command[1].isBlank()) {
                        System.out.println("Укажите задачу для добавления.");
                    } else {
                        todoList.add(command[1].trim());
                        System.out.println("Задача добавлена.");
                    }
                }
                case "EDIT" -> {
                    if (command.length < 2 || command[1].isBlank()) {
                        System.out.println("Укажите номер задачи и новую задачу.");
                    } else {
                        String[] parts = command[1].split(" ", 2);
                        if (parts.length < 2 || parts[1].isBlank()) {
                            System.out.println("Укажите номер задачи и новую задачу.");
                        } else {
                            try {
                                int index = Integer.parseInt(parts[0]) - 1;
                                todoList.edit(index, parts[1].trim());
                                System.out.println("Задача отредактирована.");
                            } catch (NumberFormatException e) {
                                System.out.println("Неверный формат номера задачи.");
                            }
                        }
                    }
                }
                case "DELETE" -> {
                    if (command.length < 2 || command[1].isBlank()) {
                        System.out.println("Укажите номер задачи для удаления.");
                    } else {
                        String numStr = command[1].trim().split(" ", 2)[0];
                        try {
                            int index = Integer.parseInt(numStr) - 1;
                            todoList.delete(index);
                            System.out.println("Задача удалена.");
                        } catch (NumberFormatException e) {
                            System.out.println("Неверный формат номера задачи.");
                        }
                    }
                }
                case "EXIT" -> {
                    System.out.println("Выход из программы.");
                    in.close();
                    return;
                }
                default -> System.out.println("Неизвестная команда. Попробуйте снова.");
            }
        }
    }
}
/* Пример ввода в консоль:
ADD Buy milk
ADD Learn java
EDIT 3 Buy coffee
 */
