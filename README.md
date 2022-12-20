КРАТКАЯ ИНФОРМАЦИЯ О РЕПОЗИТОРИИ  
  
   Данный проект это система из сервера и телеграм бота. Суть проекта заключается в сборе информации с разных сайтов о различных мероприятиях в сфере информационных технологий. Последующая обработка заключается в фильтрации, хранение в базе данных, и выдаче по апи боту. 
Документация на апи - https://documenter.getpostman.com/view/21209661/2s84DrQMTV
 
 Весь проект для удобства упакован в докер. 





ИНСТРУКЦИЯ ПО ЭКСПЛУАТАЦИИ ИНФОРМАЦИОННОЙ СИСТЕМЫ

Для запуска всех контейнеров, а также для их базовой настройки необходимо выполнить ряд действий. Весь текст в кавычках после слова «CMD» необходимо выполнять в терминале.
1.	Для начала нужно запустить все контейнеры через docker-compose, файл находится в корне проекта. CMD «docker-compose up —build».
2.	После запуска всех контейнеров нужно собрать статические файлы, такие как CSS, JS и т. д. Это нужно, чтобы эти файлы раздавал nginx. CMD «docker exec django python3 manage.py collectstatic».
3.	Далее нужно создать суперпользователя для администрирования БД. Данное действие выполняется только при первом запуске или после удаления информации из БД. CMD «docker exec -it django python3 manage.py createsuperuser». После этого будет необходимо ввести данные пользователя.
4.	Для дальнейшей настройки необходимо перейти по адресу «адрес_сервера/admin» и ввести логин и пароль ранее созданного пользователя. 
5.	Перейти в раздел «Intervals» и добавить 2 интервала: первый для запуска задачи сбора новых мероприятий, а второй для очистки БД от старых. Для сбора мероприятий рекомендуется создать интервал, равный 30 минутам, а для очистки БД равный 1 дню. При желании можно создать любой интервал для данных задач. Параметры для настройки: «Number of Periods» - единица времени интервала, «Interval Period» - величина измерения интервала.
6.	Перейти в раздел «Periodic tasks» и добавить соответствующие задачи. При создании обязательно указывается название задачи (Name), сама выполняемая задача (Task (registered)), которая будет выполняться периодически (сбор новых мероприятий, очистка БД), а также интервал выполнения (Interval Schedule), созданный в предыдущем пункте.
7.	Для запуска созданных в пункте 6 задач вручную – необходимо выбрать нужную задачу, в поле «Action» выбрать «Run selected tasks» и нажать «Go».
