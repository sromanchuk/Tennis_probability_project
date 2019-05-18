## Tennis_probability_project ##
# Credits #
Sofiya Romanchuk and Danylo Nazaruk 
# Description #
Tennis_probability_project is a course work from the course "Programming fundamentals". 
The theme of this project is "Probability of winning of certain player in given tennis match". You can find more information on wiki. Our project is now in progress. Its idea is to calculate the formula to count the probability of the winning of particular tennis player against his opponent in tennis match.
In the Wiki you are able to find the 1st stage and later the rest 4 stages of my project, each lasts 2 weeks. And the last, fifth one will end on 12.05.2019. There you could also find weekly reports. All the information in Wiki is on ukrainian.
In the 1 stage you could find the theme, system requirements, description of this course work, description of the functionality of the API and the weekly reports.
In the 2 stage you could find functional system requirements, non-functional system requirements, description of the input data, description of the capabilities of modules, module packages, libraries that will be used to work with data in the program, description of the organization of group work on the project.
### Призначення та коротка характеристика програми ###
Ця програма призначена для визначення імовірного переможця тенісного турніру за заданими користувачем параметрами. 

Вхідні дані програми: ім'я першого тенісного гравця, ім'я другого тенісного гравця, тип корту та стать обох гравців. Вибір тенісиста/тенісистки обмежується рейтингом топ 446 ATP для чоловіків та топ 392 WTA для жінок. 4 типи корту на вибір - outdoor hard, indoor hard, clay, grass. Статі - female/male.

Вихідні дані: ім'я тенісиста, який імовірно виграє, вирахуваний відсоток із яким він імовірно переможе, ім'я імовірно переможеного та тип корту, на якому повинен бути проведенй матч.

Користувач отримує інформацію про те, хто ж імовірно із двох попередньо введених тенісистів буде переможцем тенісного матчу. 

### Коротка інструкція по користуванню програмою ###
Із самого початку потрібно перейти за посиланням, яке Ви зможете знайти у        . Перейшовши за ним здійснюйте наступні кроки:

  1 крок: вибрати із 2 поточних заданих варіантів 1 для статі - female/male. 
  
  2 крок: вибрати 1 тип корту із 4 попередньо-заданих нами, на якому повинен бути проведений турнір - outdoor hard/indoor hard/clay/grass.
  
  3 крок: ввести ім'я першого тенісного гравця - Вам знову ж таки допоможе список, який автоматично шукатиме збіжності за першимим ж символами. Пам'ятайте - гравець повинен відповідати тій статі, яку ви обрали попередньо(це можна завжди змінити).
  
  4 крок: ввести ім'я другого тенісного гравця - подальші інструкції ті ж самі, що і в 3 кроці. Проте пам'ятайте, що не можна обирати того самого гравця двічі.
  
  5 крок: натиснути кнопку "Calculate probability".
  
  6 крок: якщо всі попередні кроки були реалізовані, то на екрані вашого пристрою буде висвітлена наступна сторінка із результатом.
  
### Опис тестових прикладів для первірки працездатності програми. ###
* Перше вікно

![first_window_example](https://user-images.githubusercontent.com/47135579/57972131-38ba3880-799f-11e9-84ef-8fc3d1c02468.png)

* Друге вікно(виведений результат неробочий, це лише приклад)

![second_window_example](https://user-images.githubusercontent.com/47135579/57972137-466fbe00-799f-11e9-8864-d17678529116.png)

### Структура програми з коротким описом модулів, функцій, класів та методів. ###
Модуль neural_network.py

Цей модуль представляє собою реалізацію нейронної мережі. 

Модуль 

Цей модуль є досить великим і він складає основну базу нашої програми. У ньому ми опрацьовуємо всю інформацію надану нам Sportradar API. 
* get_json(source) - повертає json словники за ссилкою;
* matches_from_tournaments(file) - повертає id матчів різних турнірів;
* player_profile(id, rankings_path) - повертає потрібну інформацію про тенісистів;
* surface_stats(data) - повертає відсоток виграшів на різних типах кортів;
* rank(id, rankings) - повертає рейтинги тенісистів;
* previous_encounters(id1, id2, date) - вираховує відсоток перемог в попередніх матчах тих самих гравців зо відбувались до заданої дати;
* rankings(gender) - повертає список із рейтингами;
* tournaments(file, gender) - повертає список із турнірами. 

Модуль MatchesADT.py

Цей модуль містить абстрактний клас Matches. Це є клас на основі АТД стек, у нього заносяться id матчів. Методи: **add** - додає новий елемент до стеку; **pop** - видаляє та повертає елемент зі стеку; **is_empty** - повертає булевий вираз, в залежності від того чи стек пустий; **__len__** - повертає довжину стеку; **process_match**- працює із останнім елементом у стеку і повертає список із цих елементів: player id, name, player id, name, match id, ranking, surface performance, previous matches agains same opponent.  
