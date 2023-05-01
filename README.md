# Notes

Программа *Notes* реализует функции создания, хранения, изменения, удаления и просмотра заметок с возможностью сортировки по параметрам.
Программа содержит свою командную оболочку и может быть использована как извне, 
так и изнутри.
Для перехода в командную оболочку введите команду: 
```
python notes.py
```
Список команд и дополнительных параметров:

* jr - просмотр журнала заметок, отсортированного по дате создания заметки

* -d - в сочетании с командой jr для сортировки журнала по дате последнего изменения
* -t - в сочетании с командой jr для сортировки журнала по заголовку
* -r - в сочетании с командой jr для просмотра журнала в обратном порядке.
Может сочетаться с другими флагами, относящимися к команде jr.
Например: "jr -rt"
* add - создание новой заметки
* sh - просмотр заметок
* del - удаление заметки
* cg - изменение существующей заметки
* exit - выход из оболочки
* -i - указание на id заметки. 
Может использоваться в сочетании с командами sh, del, cg
* -n - указание на индекс заметки.
Может использоваться в сочетании с командами sh, del, cg
* -h - указание на заголовок заметки.
Может использоваться в сочетании с командами sh, del, cg
* --title - для ввод заглавия заметки. Заглавие нужно вводить через пробел после флага
и заключать в кавычки ("). Например: --title "Title"
* --msg - для ввода содержания заметки. Содержание нужно вводить через пробел после флага
и заключать в кавычки ("). Например: --msg "Text

Флаги `--title` и `--msg` могут быть использованы только с командами add и cg и должны располагаться в самом конце введённой строки

Если флаг не был указан, появится приглашение ко вводу дополнительных параметров.