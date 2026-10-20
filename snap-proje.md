    # Единый объединённый документ

    > В этот файл без удаления содержания включены оба исходных файла.

    ---

    # Часть 1. Справочник блоков Snap!

    # Справочник блоков Snap! — объединённая версия

    > Объединены структура и таблицы из Markdown-файла `snap_blocks_reference_ru-2.md` с подробностями и примерами значений из XML-файла `snap_all_blocks_with_descriptions.xml`.
    >
    > Важное ограничение: XML-файл содержит в основном последовательность текстовых значений, параметров и демонстрационных данных, а не полноценные определения каждого блока с однозначной привязкой. Поэтому значения ниже приведены как дополнительные примеры/контекст, когда такую связь можно установить; неизвестные соответствия явно не выдумываются.

    ## Содержание

    - [1. Обозначения](#1-обозначения)
    - [2. Как читать XML](#2-как-читать-xml)
    - [3. Motion — Движение](#3-motion--движение)
    - [4. Looks — Внешность](#4-looks--внешность)
    - [5. Sound — Звук](#5-sound--звук)
    - [6. Pen — Перо](#6-pen--перо)
    - [7. Control — Управление](#7-control--управление)
    - [8. Sensing — Сенсоры](#8-sensing--сенсоры)
    - [9. Operators — Операторы](#9-operators--операторы)
    - [10. Variables — Переменные](#10-variables--переменные)
    - [11. Lists — Списки](#11-lists--списки)
    - [12. Полная XML-модель проекта](#12-полная-xml-модель-проекта)
    - [13. Что именно хранится в XML](#13-что-именно-хранится-в-xml)

    ## 1. Обозначения

    | Обозначение | Значение |
    |---|---|
    | `command` | Команда: выполняет действие и не возвращает значение. |
    | `reporter` | Репортёр: возвращает значение; обычно имеет овальную форму. |
    | `predicate` | Логический репортёр: возвращает `true` или `false`; обычно имеет шестиугольную форму. |
    | `hat` | Шляпа: запускает скрипт по событию. |
    | `c-command` | C-блок: содержит другие блоки внутри, например цикл или условие. |
    | `%n` | Число. |
    | `%s` | Текст или обычное значение. |
    | `%b` | Логическое значение. |
    | `%obj` | Спрайт, сцена, курсор или другой объект. |
    | `%clr` | Цвет. |
    | `%k` | Клавиша. |
    | `%v` | Переменная. |
    | `%l` | Список. |
    | `%ring` | Функция или контекст в ring. |
    | `%u` | Локальная переменная цикла. |

    ## 2. Как читать XML

    В XML-проекте Snap! обычно встречаются такие элементы:

    | XML-элемент | Назначение |
    |---|---|
    | `<project>` | Корневой элемент проекта. |
    | `<stage>` | Сцена проекта. |
    | `<sprite>` | Спрайт. |
    | `<scripts>` | Контейнер скриптов объекта. |
    | `<script>` | Последовательность соединённых блоков. |
    | `<block s="...">` | Экземпляр блока; атрибут `s` содержит его XML-сигнатуру. |
    | `<l>...</l>` | Литеральное значение: число, текст, цвет или другое простое значение. |
    | `<list>...</list>` | Список или структурированное значение. |
    | `<block-definition>` | Определение пользовательского блока, если оно присутствует. |
    | `<variable>` | Описание или значение переменной, если оно присутствует в соответствующем разделе. |

    ### Главное правило

    Стандартный блок Snap! обычно хранится не как отдельное определение с полной реализацией, а как экземпляр:

    ```xml
    <block s="move %n steps">
        <l>10</l>
    </block>
    ```

    Здесь:

    - `s="move %n steps"` — идентификатор/сигнатура блока;
    - `<l>10</l>` — фактическое значение входа;
    - среда Snap! уже знает, как визуализировать и выполнять этот встроенный блок.

    ### Вложенный репортёр

    ```xml
    <block s="move %n steps">
        <block s="pick random %n to %n">
            <l>1</l>
            <l>10</l>
        </block>
    </block>
    ```

    В этом примере результат блока `pick random` используется как количество шагов для `move`.

    ### Скрипт

    ```xml
    <script x="0" y="0">
        <block s="when green flag clicked"></block>
        <block s="move %n steps"><l>10</l></block>
        <block s="turn ↻ %n degrees"><l>15</l></block>
    </script>
    ```

    Атрибуты `x` и `y` задают положение скрипта на рабочей области; они не являются входами блоков.

    ## 3. Motion — Движение

    | Блок | Тип | Назначение | XML-сигнатура | Примеры XML-значений |
    |---|---|---|---|---|
    | Move steps | command | Сдвигает спрайт вперёд на N шагов. | `move %n steps` | `10`, `15` |
    | Turn clockwise | command | Поворачивает по часовой стрелке. | `turn ↻ %n degrees` | `15`, `20` |
    | Turn counter-clockwise | command | Поворачивает против часовой стрелки. | `turn ↺ %n degrees` | `15`, `-15` |
    | Point in direction | command | Задаёт направление в градусах. | `point in direction %n` | `90`, `0` |
    | Point towards | command | Поворачивает к объекту или курсору. | `point towards %obj` | `mouse-pointer`, `Sprite1` |
    | Go to coordinates | command | Переходит в координаты X и Y. | `go to x: %n y: %n` | `0`, `10`, `-10` |
    | Go to object | command | Переходит к объекту, курсору или случайной позиции. | `go to %obj` | `mouse-pointer`, `Sprite1` |
    | Glide | command | Плавно движется к точке за N секунд. | `glide %n secs to x: %n y: %n` | `0.25`, `0`, `0` |
    | Change X | command | Сдвигает по оси X. | `change x by %n` | `10`, `-10` |
    | Change Y | command | Сдвигает по оси Y. | `change y by %n` | `10`, `-10` |
    | Set X | command | Задаёт координату X. | `set x to %n` | `0`, `50` |
    | Set Y | command | Задаёт координату Y. | `set y to %n` | `0`, `50` |
    | Bounce | command | Отскакивает от края сцены. | `if on edge, bounce` | — |
    | X position | reporter | Возвращает X-координату. | `x position` | `0`, `10`, `-10` |
    | Y position | reporter | Возвращает Y-координату. | `y position` | `0`, `10`, `-10` |
    | Direction | reporter | Возвращает направление. | `direction` | `90`, `0` |

    ### Дополнительные данные XML

    В XML присутствуют значения, связанные с объектами и позиционированием: `mouse-pointer`, `Sprite1`, `0`, `1`, `10`, `15`, `20`, `50`, а также отрицательные значения вроде `-10`. Из-за отсутствия структурных тегов в доступном фрагменте нельзя надёжно определить, к какому конкретному экземпляру блока относится каждое значение.

    ## 4. Looks — Внешность

    | Блок | Тип | Назначение | XML-сигнатура | Примеры XML-значений |
    |---|---|---|---|---|
    | Switch to costume | command | Меняет костюм на выбранный. | `switch to costume %s` | `costume1`, `costume` |
    | Next costume | command | Переключает на следующий костюм. | `next costume` | — |
    | Costume number | reporter | Возвращает номер текущего костюма. | `costume #` | `1`, `2` |
    | Say | command | Показывает реплику в облачке. | `say %s` | `Hello!`, `Hello`, `What's your name?` |
    | Say for seconds | command | Показывает реплику ограниченное время. | `say %s for %n secs` | `Hello!`, `2` |
    | Think | command | Показывает мысль в облачке. | `think %s` | `Hmm...` |
    | Think for seconds | command | Показывает мысль ограниченное время. | `think %s for %n secs` | `Hmm...`, `2` |
    | Costume property | reporter | Возвращает свойство костюма, например ширину. | `%s of costume %s` | `width`, `costume1`, `100` |
    | Stretch costume | reporter | Возвращает растянутую копию костюма. | `stretch %n x: %n y: %n %` | `100`, `100` |
    | Skew costume | reporter | Возвращает скошенную копию костюма. | `skew %n to %n degrees %n %` | `100`, `0`, `100` |
    | New costume | reporter | Создаёт новый костюм заданного размера. | `new costume %s width %n height %n` | `costume`, `100`, `100` |
    | Change graphic effect | command | Изменяет графический эффект, например `ghost`. | `change %s effect by %n` | `ghost`, `25` |
    | Set graphic effect | command | Устанавливает графический эффект. | `set %s effect to %n` | `ghost`, `0` |
    | Clear graphic effects | command | Сбрасывает все графические эффекты. | `clear graphic effects` | — |
    | Graphic effect | reporter | Возвращает значение эффекта. | `%s effect` | `ghost`, `10` |
    | Change size | command | Меняет размер спрайта. | `change size by %n %` | `10`, `100` |
    | Set size | command | Устанавливает размер спрайта. | `set size to %n %` | `100` |
    | Size | reporter | Возвращает размер спрайта. | `size` | `100` |
    | Show | command | Показывает спрайт. | `show` | — |
    | Hide | command | Скрывает спрайт. | `hide` | — |
    | Shown? | predicate | Проверяет, виден ли спрайт. | `shown?` | `true` |
    | Go to layer | command | Перемещает на передний или задний слой. | `go to %s layer` | `front`, `back` |
    | Go back layers | command | Перемещает назад на N слоёв. | `go back %n layers` | `1`, `2` |

    ## 5. Sound — Звук

    | Блок | Тип | Назначение | XML-сигнатура | Примеры XML-значений |
    |---|---|---|---|---|
    | Play sound | command | Запускает звук и продолжает выполнение. | `play sound %s` | `sound1` |
    | Play sound until done | command | Проигрывает звук и ждёт завершения. | `play sound %s until done` | `sound1` |
    | Stop all sounds | command | Останавливает все звуки. | `stop all sounds` | — |
    | Play sound at Hz | command | Проигрывает звук с указанной частотой дискретизации. | `play sound %s at %n Hz` | `sound1`, `44100` |
    | Sound property | reporter | Возвращает свойство звука, например длительность. | `%s of sound %s` | `duration`, `sound1` |
    | New sound | reporter | Создаёт новый звук из аудиоданных. | `new sound %s rate %n Hz` | `sound`, `44100` |
    | Rest | command | Делает паузу на указанное число долей. | `rest for %n beats` | `0.25`, `1` |
    | Play note | command | Играет ноту заданное количество долей. | `play note %n for %n beats` | `60`, `0.5`, `1` |
    | Set instrument | command | Выбирает музыкальный инструмент. | `set instrument to %n` | `1`, `20` |
    | Change tempo | command | Меняет темп. | `change tempo by %n` | `10` |
    | Set tempo | command | Устанавливает темп. | `set tempo to %n` | `60`, `120` |
    | Tempo | reporter | Возвращает текущий темп. | `tempo` | `60` |
    | Change volume | command | Меняет громкость. | `change volume by %n` | `10` |
    | Set volume | command | Устанавливает громкость. | `set volume to %n %` | `100` |
    | Volume | reporter | Возвращает громкость. | `volume` | `100` |
    | Change balance | command | Меняет стерео-баланс. | `change balance by %n` | `0` |
    | Set balance | command | Устанавливает стерео-баланс. | `set balance to %n` | `0` |
    | Balance | reporter | Возвращает стерео-баланс. | `balance` | `0` |
    | Play frequency | command | Включает тон заданной частоты. | `play frequency %n` | `440` |
    | Stop frequency | command | Останавливает воспроизводимый тон. | `stop frequency` | — |

    ## 6. Pen — Перо

    | Блок | Тип | Назначение | XML-сигнатура | Примеры XML-значений |
    |---|---|---|---|---|
    | Clear | command | Стирает весь рисунок пера. | `clear` | — |
    | Pen down | command | Опускает перо; движение рисует линию. | `pen down` | — |
    | Pen up | command | Поднимает перо; движение не рисует. | `pen up` | — |
    | Pen down? | predicate | Проверяет, опущено ли перо. | `pen down?` | `true` |
    | Set pen color | command | Устанавливает цвет пера. | `set pen color to %clr` | `#000000`, `#FF0000`, `#00FF00`, `#0000FF` |
    | Change pen property | command | Меняет параметр пера, например оттенок. | `change pen %s by %n` | `hue`, `10` |
    | Set pen property | command | Устанавливает параметр пера. | `set pen %s to %n` | `hue`, `0` |
    | Pen property | reporter | Возвращает параметр пера. | `pen %s` | `hue`, `1` |
    | Change pen size | command | Меняет толщину линии. | `change pen size by %n` | `5` |
    | Set pen size | command | Устанавливает толщину линии. | `set pen size to %n` | `1`, `5` |
    | Stamp | command | Отпечатывает текущий костюм спрайта. | `stamp` | — |
    | Fill | command | Заливает область цветом. | `fill` | — |
    | Write | command | Пишет текст на сцене. | `write %s size %n` | `Hello`, `20` |
    | Pen trails | reporter | Возвращает рисунок пера как изображение. | `pen trails` | — |
    | Paste | command | Вставляет костюм на объект. | `paste %s on %obj` | `costume1`, `Sprite1` |
    | Cut | reporter | Вырезает изображение с объекта. | `cut from %obj` | `Sprite1` |
    | Draw | command | Рисует на объекте. | `draw %s on %obj` | `paint`, `Stage` |
    | Color | reporter | Представляет цвет как значение. | `color %clr` | `#000000` |
    | Color component | reporter | Возвращает компонент цвета. | `%n of color %clr` | `0`, `1`, `255` |
    | New color | reporter | Создаёт цвет из цветовых компонентов. | `new color %clr %clr %clr` | `#000000`, `#FF0000`, `#00FF00`, `#0000FF` |
    | Color equality | predicate | Сравнивает два цвета. | `%clr = %clr` | `true`, `false` |

    ## 7. Control — Управление

    | Блок | Тип | Назначение | XML-сигнатура | Примеры XML-значений |
    |---|---|---|---|---|
    | Green flag | hat | Запускает скрипт по нажатию зелёного флага. | `when green flag clicked` | — |
    | When edited | hat | Запускает скрипт при изменении значения. | `when %s is edited` | `variable`, `value` |
    | Clone start | hat | Запускает скрипт при создании клона. | `when I start as a clone` | — |
    | Receive message | hat | Запускает скрипт при получении сообщения. | `when I receive %s` | `message1`, `clicked` |
    | Key pressed | hat | Запускает скрипт при нажатии клавиши. | `when %k key pressed` | `space` |
    | When condition | hat | Запускает скрипт, когда условие становится истинным. | `when %b` | `true` |
    | When I am | hat | Запускает скрипт по событию взаимодействия. | `when I am %s` | `clicked` |
    | Broadcast | command | Отправляет сообщение всем объектам. | `broadcast %s` | `message1` |
    | Broadcast and wait | command | Отправляет сообщение и ждёт завершения обработчиков. | `broadcast %s and wait` | `message1` |
    | Request | reporter | Отправляет запрос и возвращает ответ. | `request %s` | `message1`, `value` |
    | Wait | command | Ждёт N секунд. | `wait %n secs` | `1`, `2` |
    | Wait until | command | Ждёт, пока условие не станет истинным. | `wait until %b` | `true` |
    | Forever | c-command | Бесконечно повторяет вложенные команды. | `forever` | — |
    | Repeat | c-command | Повторяет вложенные команды N раз. | `repeat %n` | `10` |
    | Repeat until | c-command | Повторяет вложенные команды до истинности условия. | `repeat until %b` | `true` |
    | For | c-command | Выполняет цикл со счётчиком от начала до конца. | `for %u = %n to %n` | `i`, `1`, `10` |
    | If | c-command | Выполняет вложенные команды, если условие истинно. | `if %b then` | `true` |
    | If else | c-command | Выбирает одну из двух ветвей. | `if %b then else` | `true`, `yes`, `no` |
    | If else reporter | reporter | Возвращает одно из двух значений по условию. | `if %b then %s else %s` | `true`, `yes`, `no` |
    | Report | command | Возвращает значение из пользовательского блока. | `report %s` | `value` |
    | Stop | command | Останавливает скрипт, спрайт или всё выполнение. | `stop %s` | `this script`, `Sprite1`, `all` |
    | Run | command | Выполняет функцию в ring и ждёт. | `run %ring` | `script` |
    | Launch | command | Запускает функцию в ring параллельно. | `launch %ring` | `script` |
    | Call | reporter | Вызывает функцию в ring и возвращает результат. | `call %ring` | `script`, `value` |
    | Pipe | reporter | Передаёт результат одной функции другой. | `%ring ▶ %ring` | `script` |
    | Tell | command | Просит другой объект выполнить функцию. | `tell %obj to %ring` | `Sprite1`, `myself` |
    | Ask object | reporter | Запрашивает у другого объекта результат функции. | `ask %obj for %ring` | `Sprite1`, `value` |
    | Create clone | command | Создаёт клон выбранного объекта. | `create a clone of %obj` | `Sprite1` |
    | New clone | reporter | Создаёт клон и возвращает ссылку на него. | `a new clone of %obj` | `Sprite1` |
    | Delete clone | command | Удаляет текущий клон. | `delete this clone` | — |
    | Pause all | command | Ставит выполнение всех скриптов на паузу. | `pause all` | — |
    | Switch scene | command | Переключает сцену. | `switch to scene %s` | `Scene1` |
    | Define | command | Создаёт пользовательский блок программно. | `define %ring` | `block name`, `label` |
    | Delete block | command | Удаляет пользовательский блок. | `delete block %s` | `block name` |
    | Set block property | command | Меняет свойство пользовательского блока. | `set %s of block %s to %s` | `label`, `block name`, `new label` |
    | Block property | reporter | Возвращает свойство пользовательского блока. | `%s of block %s` | `label`, `block name` |
    | This | reporter | Возвращает текущий скрипт или контекст. | `this %s` | `script`, `value` |
    | Set slot | command | Задаёт значение слота блока. | `set slot %n to %s` | `1`, `value` |

    ## 8. Sensing — Сенсоры

    | Блок | Тип | Назначение | XML-сигнатура | Примеры XML-значений |
    |---|---|---|---|---|
    | Touching? | predicate | Проверяет касание объекта, края или курсора. | `touching %obj ?` | `mouse-pointer`, `Sprite1` |
    | Color touching color? | predicate | Проверяет соприкосновение двух цветов. | `color %clr is touching %clr ?` | `#000000`, `#FFFFFF` |
    | Ask and wait | command | Задаёт вопрос пользователю и ждёт ответ. | `ask %s and wait` | `What's your name?` |
    | Answer | reporter | Возвращает последний ответ пользователя. | `answer` | — |
    | Mouse position | reporter | Возвращает позицию мыши. | `mouse position` | `0`, `0` |
    | Mouse X | reporter | Возвращает X-координату мыши. | `mouse x` | `0` |
    | Mouse Y | reporter | Возвращает Y-координату мыши. | `mouse y` | `0` |
    | Mouse down? | predicate | Проверяет, нажата ли кнопка мыши. | `mouse down?` | `true`, `false` |
    | Key pressed? | predicate | Проверяет состояние указанной клавиши. | `key %k pressed?` | `space`, `true` |
    | Relation to object | reporter | Возвращает отношение к объекту, например расстояние. | `%s to %obj` | `distance`, `mouse-pointer` |
    | Value at object | reporter | Возвращает параметр в точке или у объекта. | `%s at %obj` | `color`, `mouse-pointer` |
    | Reset timer | command | Сбрасывает секундомер. | `reset timer` | — |
    | Timer | reporter | Возвращает время с последнего сброса. | `timer` | — |
    | Current date/time | reporter | Возвращает выбранную часть даты или времени. | `current %s` | `year` |
    | Property of object | reporter | Возвращает свойство другого спрайта. | `%s of %obj` | `x position`, `Sprite1` |
    | My property | reporter | Возвращает свойство текущего спрайта. | `my %s` | `neighbors` |
    | Object | reporter | Возвращает ссылку на объект по имени. | `object %s` | `Sprite1` |
    | URL | reporter | Загружает содержимое URL. | `url %s` | `https://example.com` |
    | Microphone | reporter | Возвращает данные микрофона, например громкость. | `microphone %s` | `loudness` |
    | Video | reporter | Возвращает данные камеры, например движение. | `video %s on %obj` | `motion`, `Stage` |
    | Video transparency | command | Устанавливает прозрачность видео. | `set video transparency to %n %` | `50` |
    | Setting enabled? | predicate | Проверяет глобальную настройку. | `is %s on?` | `turbo mode`, `true` |
    | Set setting | command | Меняет глобальную настройку. | `set %s to %b` | `turbo mode`, `true` |

    ## 9. Operators — Операторы

    | Блок | Тип | Назначение | XML-сигнатура | Примеры XML-значений |
    |---|---|---|---|---|
    | Add | reporter | Складывает два числа. | `%n + %n` | `0`, `1`, `10` |
    | Subtract | reporter | Вычитает второе значение из первого. | `%n - %n` | `0`, `1`, `10` |
    | Multiply | reporter | Умножает числа. | `%n × %n` | `0`, `1`, `10` |
    | Divide | reporter | Делит первое число на второе. | `%n ÷ %n` | `0`, `1`, `10` |
    | Power | reporter | Возводит число в степень. | `%n ^ %n` | `0`, `1`, `10` |
    | Modulo | reporter | Возвращает остаток от деления. | `%n mod %n` | `0`, `1`, `10` |
    | Min | reporter | Возвращает минимум из двух чисел. | `min %n %n` | `0`, `1`, `10` |
    | Max | reporter | Возвращает максимум из двух чисел. | `max %n %n` | `0`, `1`, `10` |
    | Round | reporter | Округляет число. | `round %n` | `0`, `1`, `10` |
    | Math function | reporter | Выполняет математическую функцию. | `%s of %n` | `sqrt`, `0`, `1` |
    | Atan2 | reporter | Вычисляет арктангенс двух аргументов. | `atan2 %n %n` | `0`, `1`, `10` |
    | Random | reporter | Возвращает случайное число в диапазоне. | `pick random %n to %n` | `1`, `10` |
    | Less than | predicate | Проверяет, меньше ли первое значение второго. | `%n < %n` | `0`, `1`, `10` |
    | Equal | predicate | Проверяет равенство значений. | `%n = %n` | `0`, `1`, `true` |
    | Greater than | predicate | Проверяет, больше ли первое значение второго. | `%n > %n` | `0`, `1`, `10` |
    | And | predicate | Логическое И. | `%b and %b` | `true`, `false` |
    | Or | predicate | Логическое ИЛИ. | `%b or %b` | `true`, `false` |
    | Not | predicate | Логическое НЕ. | `not %b` | `true`, `false` |
    | True-false | reporter | Преобразует булево значение в число. | `true-false %b` | `true`, `false` |
    | Join | reporter | Склеивает текстовые значения. | `join %s %s` | `Hello`, `World`, `HelloWorld` |
    | Split | reporter | Разбивает текст по разделителю. | `split %s at %s` | `Hello,World`, `,` |
    | Letter | reporter | Возвращает символ по позиции. | `letter %n of %s` | `1`, `Hello`, `H` |
    | Text property | reporter | Возвращает свойство текста, например длину. | `%s of text %s` | `length`, `Hello` |
    | Unicode of | reporter | Возвращает Unicode-код символа. | `unicode of %s` | `A`, `65` |
    | Unicode as letter | reporter | Преобразует Unicode-код в символ. | `unicode %n as letter` | `65`, `A` |
    | Is type? | predicate | Проверяет тип значения. | `is %s a %s ?` | `value`, `number` |
    | Is identical? | predicate | Проверяет тождественность объектов. | `is %s identical to %s ?` | `variable`, `value` |

    ## 10. Variables — Переменные

    | Блок | Тип | Назначение | XML-сигнатура | Примеры XML-значений |
    |---|---|---|---|---|
    | Set variable | command | Присваивает переменной значение. | `set %v to %s` | `variable`, `value` |
    | Change variable | command | Увеличивает значение переменной. | `change %v by %n` | `variable`, `1` |
    | Show variable | command | Показывает переменную на сцене. | `show variable %v` | `variable` |
    | Hide variable | command | Скрывает переменную на сцене. | `hide variable %v` | `variable` |
    | Inherit | reporter | Возвращает наследуемое клоном значение оригинала. | `inherit %v` | `variable` |

    ## 11. Lists — Списки

    | Блок | Тип | Назначение | XML-сигнатура | Примеры XML-значений |
    |---|---|---|---|---|
    | List | reporter | Создаёт список. | `list %s` | `item`, `1`, `10` |
    | Numbers from/to | reporter | Создаёт последовательность чисел. | `numbers from %n to %n` | `1`, `10` |
    | In front of | reporter | Добавляет элемент в начало списка. | `%s in front of %l` | `item`, `new item` |
    | Item of | reporter | Возвращает элемент списка по индексу. | `item %n of %l` | `1`, `item` |
    | All but first | reporter | Возвращает список без первого элемента. | `all but first of %l` | `item` |
    | List property | reporter | Возвращает свойство списка, например длину. | `%s of %l` | `length`, `item` |
    | Index of | reporter | Возвращает индекс элемента. | `index of %s in %l` | `item`, `1` |
    | Contains? | predicate | Проверяет наличие элемента. | `%l contains %s ?` | `item`, `true` |
    | Is empty? | predicate | Проверяет, пуст ли список. | `is %l empty?` | `item`, `true` |
    | Map | reporter | Применяет функцию к каждому элементу. | `map %ring over %l` | `i`, `item` |
    | Keep | reporter | Оставляет элементы, удовлетворяющие условию. | `keep %b from %l` | `true`, `item` |
    | Find first | reporter | Ищет первый подходящий элемент. | `find first %s in %l` | `item` |
    | Combine | reporter | Сворачивает список функцией. | `combine %l using %ring` | `item`, `i` |
    | For each | c-command | Выполняет команды для каждого элемента. | `for each %u in %l` | `i`, `item` |
    | Add | command | Добавляет элемент в конец списка. | `add %s to %l` | `new item`, `item` |
    | Delete | command | Удаляет элемент по индексу. | `delete %n of %l` | `1`, `item` |
    | Insert | command | Вставляет элемент по индексу. | `insert %s at %n of %l` | `new item`, `1`, `item` |
    | Replace | command | Заменяет элемент по индексу. | `replace item %n of %l with %s` | `1`, `item`, `new item` |
    | Append | reporter | Склеивает два списка. | `append %l %l` | `item`, `new item` |
    | Reshape | reporter | Меняет форму списка, создавая многомерную структуру. | `reshape %l to %n` | `item`, `2` |
    | Combinations | reporter | Возвращает все комбинации элементов. | `combinations of %l` | `item` |

    ## 12. Полная XML-модель проекта

    Ниже приведён минимальный пример, показывающий структуру, в которую обычно вкладываются экземпляры блоков:

    ```xml
    <project collabStartIndex="0">
        <notes></notes>
        <thumbnail>...</thumbnail>
        <stage name="Stage">
            <pentrails></pentrails>
            <costumes>
                <list>
                    <item name="costume1">...</item>
                </list>
            </costumes>
            <sounds>
                <list>
                    <item name="sound1">...</item>
                </list>
            </sounds>
            <variables>
                <variable name="variable">value</variable>
            </variables>
            <scripts>
                <script x="0" y="0">
                    <block s="when green flag clicked"></block>
                    <block s="set %v to %s">
                        <l>variable</l>
                        <l>value</l>
                    </block>
                </script>
            </scripts>
            <sprites>
                <sprite name="Sprite1">
                    <scripts>
                        <script x="0" y="0">
                            <block s="when green flag clicked"></block>
                            <block s="move %n steps"><l>10</l></block>
                        </script>
                    </scripts>
                </sprite>
            </sprites>
        </stage>
    </project>
    ```

    ### Практическая интерпретация

    1. Сначала читается объект: сцена или спрайт.
    2. Затем ищется его контейнер `<scripts>`.
    3. Внутри `<script>` блоки идут в порядке выполнения.
    4. У каждого `<block>` атрибут `s` показывает сигнатуру.
    5. Дочерние `<l>` и `<block>` являются входами текущего блока.
    6. Вложенные C-блоки дополнительно содержат скрипты или группы вложенных блоков.

    ## 13. Что именно хранится в XML

    | Что хранится | Где | Комментарий |
    |---|---|---|
    | Экземпляр встроенного блока | `<block s="...">` | Содержит конкретный блок, используемый в проекте. |
    | Вход блока | `<l>...</l>` или дочерний `<block>` | Это фактическое значение или вычисляемый вход. |
    | Скрипт | `<script>` | Цепочка соединённых блоков. |
    | Положение скрипта на холсте | `x` и `y` у `<script>` | Координаты отображения, а не аргументы блока. |
    | Переменная | Раздел переменных объекта или сцены | Имя и текущее значение зависят от структуры проекта. |
    | Костюм | Раздел `<costumes>` | Может ссылаться на `costume1` и другие ресурсы. |
    | Звук | Раздел `<sounds>` | Может ссылаться на `sound1` и другие ресурсы. |
    | Пользовательский блок | `<block-definition>` или связанный раздел | Содержит интерфейс и тело пользовательского блока, если определён. |
    | Реализация встроенного блока | Не в экземпляре XML-проекта | Она находится в исходном коде среды Snap!, а не в каждой копии проекта. |

    ## Ограничения объединения

    - Исходный Markdown содержит структурированный справочник: категории, названия, типы, назначения и сигнатуры.
    - Исходный XML-файл в доступном виде содержит последовательность значений, но не предоставляет для каждого значения полный родительский путь и однозначный идентификатор блока.
    - Поэтому примеры в колонке `Примеры XML-значений` — это подтверждённые или очевидно совместимые значения из XML, а не восстановленная точная трассировка каждого XML-узла.
    - Если нужна точная реконструкция исходного XML, необходим XML с сохранёнными тегами и атрибутами, а не только извлечённый текстовый фрагмент.



    вот xml файл со всей структурой 

    <blocks app="Snap! 8.0, http://snap.berkeley.edu" version="1">
    <!--
    Полный список стандартных блоков Snap! (8 категорий) с русскими описаниями.
    Это XML-представление определений блоков (block-definition),
    пригодное для импорта как библиотеки блоков в Snap!.
    Формат: <block-definition> внутри <blocks>.
    type: "command" | "reporter" | "predicate" | "hat" | "c-command"
    category: "motion" | "looks" | "sound" | "pen" | "control" | "sensing" | "operators" | "variables" | "lists"
    category-ru: русское название категории
    s: текстовая метка блока с плейсхолдерами входов (%n, %s, %b, %clr, %obj, %c, %ring и т.п.)
    description: краткое описание действия блока на русском
    -->

    <!-- ==================== MOTION (Движение) ==================== -->
    <block-definition s="move %n steps" type="command" category="motion" category-ru="Движение" description="Сдвигает спрайт вперёд на N шагов"><header></header><code></code><translations></translations><inputs><input type="%n">10</input></inputs></block-definition>
    <block-definition s="turn ↻ %n degrees" type="command" category="motion" category-ru="Движение" description="Поворачивает по часовой стрелке"><header></header><code></code><translations></translations><inputs><input type="%n">15</input></inputs></block-definition>
    <block-definition s="turn ↺ %n degrees" type="command" category="motion" category-ru="Движение" description="Поворачивает против часовой стрелки"><header></header><code></code><translations></translations><inputs><input type="%n">15</input></inputs></block-definition>
    <block-definition s="point in direction %n" type="command" category="motion" category-ru="Движение" description="Задаёт направление в градусах"><header></header><code></code><translations></translations><inputs><input type="%n">90</input></inputs></block-definition>
    <block-definition s="point towards %obj" type="command" category="motion" category-ru="Движение" description="Поворачивает спрайт к объекту или курсору"><header></header><code></code><translations></translations><inputs><input type="%obj">mouse-pointer</input></inputs></block-definition>
    <block-definition s="go to x: %n y: %n" type="command" category="motion" category-ru="Движение" description="Переходит в координаты"><header></header><code></code><translations></translations><inputs><input type="%n">0</input><input type="%n">0</input></inputs></block-definition>
    <block-definition s="go to %obj" type="command" category="motion" category-ru="Движение" description="Переходит к объекту, курсору или случайной позиции"><header></header><code></code><translations></translations><inputs><input type="%obj">mouse-pointer</input></inputs></block-definition>
    <block-definition s="glide %n secs to x: %n y: %n" type="command" category="motion" category-ru="Движение" description="Плавно едет в точку за N секунд"><header></header><code></code><translations></translations><inputs><input type="%n">1</input><input type="%n">0</input><input type="%n">0</input></inputs></block-definition>
    <block-definition s="change x by %n" type="command" category="motion" category-ru="Движение" description="Сдвигает по оси X на величину"><header></header><code></code><translations></translations><inputs><input type="%n">10</input></inputs></block-definition>
    <block-definition s="change y by %n" type="command" category="motion" category-ru="Движение" description="Сдвигает по оси Y на величину"><header></header><code></code><translations></translations><inputs><input type="%n">10</input></inputs></block-definition>
    <block-definition s="set x to %n" type="command" category="motion" category-ru="Движение" description="Задаёт координату X"><header></header><code></code><translations></translations><inputs><input type="%n">0</input></inputs></block-definition>
    <block-definition s="set y to %n" type="command" category="motion" category-ru="Движение" description="Задаёт координату Y"><header></header><code></code><translations></translations><inputs><input type="%n">0</input></inputs></block-definition>
    <block-definition s="if on edge, bounce" type="command" category="motion" category-ru="Движение" description="Отскакивает от края сцены"><header></header><code></code><translations></translations><inputs></inputs></block-definition>
    <block-definition s="x position" type="reporter" category="motion" category-ru="Движение" description="Возвращает координату X"><header></header><code></code><translations></translations><inputs></inputs></block-definition>
    <block-definition s="y position" type="reporter" category="motion" category-ru="Движение" description="Возвращает координату Y"><header></header><code></code><translations></translations><inputs></inputs></block-definition>
    <block-definition s="direction" type="reporter" category="motion" category-ru="Движение" description="Возвращает направление"><header></header><code></code><translations></translations><inputs></inputs></block-definition>

    <!-- ==================== LOOKS (Внешность) ==================== -->
    <block-definition s="switch to costume %s" type="command" category="looks" category-ru="Внешность" description="Меняет костюм на выбранный"><header></header><code></code><translations></translations><inputs><input type="%s">costume1</input></inputs></block-definition>
    <block-definition s="next costume" type="command" category="looks" category-ru="Внешность" description="Меняет костюм на следующий"><header></header><code></code><translations></translations><inputs></inputs></block-definition>
    <block-definition s="costume #" type="reporter" category="looks" category-ru="Внешность" description="Номер текущего костюма"><header></header><code></code><translations></translations><inputs></inputs></block-definition>
    <block-definition s="say %s" type="command" category="looks" category-ru="Внешность" description="Реплика в облачке"><header></header><code></code><translations></translations><inputs><input type="%s">Hello!</input></inputs></block-definition>
    <block-definition s="say %s for %n secs" type="command" category="looks" category-ru="Внешность" description="Реплика в облачке с таймером"><header></header><code></code><translations></translations><inputs><input type="%s">Hello!</input><input type="%n">2</input></inputs></block-definition>
    <block-definition s="think %s" type="command" category="looks" category-ru="Внешность" description="Мысль в облачке"><header></header><code></code><translations></translations><inputs><input type="%s">Hmm...</input></inputs></block-definition>
    <block-definition s="think %s for %n secs" type="command" category="looks" category-ru="Внешность" description="Мысль в облачке с таймером"><header></header><code></code><translations></translations><inputs><input type="%s">Hmm...</input><input type="%n">2</input></inputs></block-definition>
    <block-definition s="%s of costume %s" type="reporter" category="looks" category-ru="Внешность" description="Свойство костюма (например, ширина)"><header></header><code></code><translations></translations><inputs><input type="%s">width</input><input type="%s">costume1</input></inputs></block-definition>
    <block-definition s="stretch %n x: %n y: %n %" type="reporter" category="looks" category-ru="Внешность" description="Возвращает растянутую копию костюма"><header></header><code></code><translations></translations><inputs><input type="%n">100</input><input type="%n">100</input><input type="%n">100</input></inputs></block-definition>
    <block-definition s="skew %n to %n degrees %n %" type="reporter" category="looks" category-ru="Внешность" description="Возвращает скошенную копию костюма"><header></header><code></code><translations></translations><inputs><input type="%n">0</input><input type="%n">0</input><input type="%n">100</input></inputs></block-definition>
    <block-definition s="new costume %s width %n height %n" type="reporter" category="looks" category-ru="Внешность" description="Создаёт новый костюм заданного размера"><header></header><code></code><translations></translations><inputs><input type="%s">costume</input><input type="%n">100</input><input type="%n">100</input></inputs></block-definition>
    <block-definition s="change %s effect by %n" type="command" category="looks" category-ru="Внешность" description="Меняет графический эффект (например, ghost)"><header></header><code></code><translations></translations><inputs><input type="%s">ghost</input><input type="%n">25</input></inputs></block-definition>
    <block-definition s="set %s effect to %n" type="command" category="looks" category-ru="Внешность" description="Задаёт графический эффект"><header></header><code></code><translations></translations><inputs><input type="%s">ghost</input><input type="%n">0</input></inputs></block-definition>
    <block-definition s="clear graphic effects" type="command" category="looks" category-ru="Внешность" description="Сбрасывает эффекты"><header></header><code></code><translations></translations><inputs></inputs></block-definition>
    <block-definition s="%s effect" type="reporter" category="looks" category-ru="Внешность" description="Текущее значение эффекта"><header></header><code></code><translations></translations><inputs><input type="%s">ghost</input></inputs></block-definition>
    <block-definition s="change size by %n %" type="command" category="looks" category-ru="Внешность" description="Меняет размер"><header></header><code></code><translations></translations><inputs><input type="%n">10</input></inputs></block-definition>
    <block-definition s="set size to %n %" type="command" category="looks" category-ru="Внешность" description="Задаёт размер"><header></header><code></code><translations></translations><inputs><input type="%n">100</input></inputs></block-definition>
    <block-definition s="size" type="reporter" category="looks" category-ru="Внешность" description="Возвращает размер"><header></header><code></code><translations></translations><inputs></inputs></block-definition>
    <block-definition s="show" type="command" category="looks" category-ru="Внешность" description="Показывает спрайт"><header></header><code></code><translations></translations><inputs></inputs></block-definition>
    <block-definition s="hide" type="command" category="looks" category-ru="Внешность" description="Скрывает спрайт"><header></header><code></code><translations></translations><inputs></inputs></block-definition>
    <block-definition s="shown?" type="predicate" category="looks" category-ru="Внешность" description="Проверяет видимость"><header></header><code></code><translations></translations><inputs></inputs></block-definition>
    <block-definition s="go to %s layer" type="command" category="looks" category-ru="Внешность" description="Меняет порядок слоёв (front/back)"><header></header><code></code><translations></translations><inputs><input type="%s">front</input></inputs></block-definition>
    <block-definition s="go back %n layers" type="command" category="looks" category-ru="Внешность" description="Меняет порядок слоёв (назад на N)"><header></header><code></code><translations></translations><inputs><input type="%n">1</input></inputs></block-definition>

    <!-- ==================== SOUND (Звук) ==================== -->
    <block-definition s="play sound %s" type="command" category="sound" category-ru="Звук" description="Проигрывает звук"><header></header><code></code><translations></translations><inputs><input type="%s">sound1</input></inputs></block-definition>
    <block-definition s="play sound %s until done" type="command" category="sound" category-ru="Звук" description="Проигрывает звук и ждёт конца"><header></header><code></code><translations></translations><inputs><input type="%s">sound1</input></inputs></block-definition>
    <block-definition s="stop all sounds" type="command" category="sound" category-ru="Звук" description="Останавливает все звуки"><header></header><code></code><translations></translations><inputs></inputs></block-definition>
    <block-definition s="play sound %s at %n Hz" type="command" category="sound" category-ru="Звук" description="Проигрывает с изменённой частотой дискретизации"><header></header><code></code><translations></translations><inputs><input type="%s">sound1</input><input type="%n">44100</input></inputs></block-definition>
    <block-definition s="%s of sound %s" type="reporter" category="sound" category-ru="Звук" description="Свойство звука (например, длительность)"><header></header><code></code><translations></translations><inputs><input type="%s">duration</input><input type="%s">sound1</input></inputs></block-definition>
    <block-definition s="new sound %s rate %n Hz" type="reporter" category="sound" category-ru="Звук" description="Создаёт новый звук из данных"><header></header><code></code><translations></translations><inputs><input type="%s">sound</input><input type="%n">44100</input></inputs></block-definition>
    <block-definition s="rest for %n beats" type="command" category="sound" category-ru="Звук" description="Пауза в долях"><header></header><code></code><translations></translations><inputs><input type="%n">0.25</input></inputs></block-definition>
    <block-definition s="play note %n for %n beats" type="command" category="sound" category-ru="Звук" description="Играет ноту"><header></header><code></code><translations></translations><inputs><input type="%n">60</input><input type="%n">0.5</input></inputs></block-definition>
    <block-definition s="set instrument to %n" type="command" category="sound" category-ru="Звук" description="Выбирает инструмент"><header></header><code></code><translations></translations><inputs><input type="%n">1</input></inputs></block-definition>
    <block-definition s="change tempo by %n" type="command" category="sound" category-ru="Звук" description="Меняет темп"><header></header><code></code><translations></translations><inputs><input type="%n">20</input></inputs></block-definition>
    <block-definition s="set tempo to %n" type="command" category="sound" category-ru="Звук" description="Задаёт темп"><header></header><code></code><translations></translations><inputs><input type="%n">60</input></inputs></block-definition>
    <block-definition s="tempo" type="reporter" category="sound" category-ru="Звук" description="Возвращает темп"><header></header><code></code><translations></translations><inputs></inputs></block-definition>
    <block-definition s="change volume by %n" type="command" category="sound" category-ru="Звук" description="Меняет громкость"><header></header><code></code><translations></translations><inputs><input type="%n">10</input></inputs></block-definition>
    <block-definition s="set volume to %n %" type="command" category="sound" category-ru="Звук" description="Задаёт громкость"><header></header><code></code><translations></translations><inputs><input type="%n">100</input></inputs></block-definition>
    <block-definition s="volume" type="reporter" category="sound" category-ru="Звук" description="Возвращает громкость"><header></header><code></code><translations></translations><inputs></inputs></block-definition>
    <block-definition s="change balance by %n" type="command" category="sound" category-ru="Звук" description="Меняет стерео-баланс"><header></header><code></code><translations></translations><inputs><input type="%n">0</input></inputs></block-definition>
    <block-definition s="set balance to %n" type="command" category="sound" category-ru="Звук" description="Задаёт стерео-баланс"><header></header><code></code><translations></translations><inputs><input type="%n">0</input></inputs></block-definition>
    <block-definition s="balance" type="reporter" category="sound" category-ru="Звук" description="Возвращает стерео-баланс"><header></header><code></code><translations></translations><inputs></inputs></block-definition>
    <block-definition s="play frequency %n" type="command" category="sound" category-ru="Звук" description="Включает тон заданной частоты"><header></header><code></code><translations></translations><inputs><input type="%n">440</input></inputs></block-definition>
    <block-definition s="stop frequency" type="command" category="sound" category-ru="Звук" description="Останавливает тон"><header></header><code></code><translations></translations><inputs></inputs></block-definition>

    <!-- ==================== PEN (Перо) ==================== -->
    <block-definition s="clear" type="command" category="pen" category-ru="Перо" description="Стирает нарисованное"><header></header><code></code><translations></translations><inputs></inputs></block-definition>
    <block-definition s="pen down" type="command" category="pen" category-ru="Перо" description="Опускает перо"><header></header><code></code><translations></translations><inputs></inputs></block-definition>
    <block-definition s="pen up" type="command" category="pen" category-ru="Перо" description="Поднимает перо"><header></header><code></code><translations></translations><inputs></inputs></block-definition>
    <block-definition s="pen down?" type="predicate" category="pen" category-ru="Перо" description="Проверяет состояние пера"><header></header><code></code><translations></translations><inputs></inputs></block-definition>
    <block-definition s="set pen color to %clr" type="command" category="pen" category-ru="Перо" description="Задаёт цвет пера"><header></header><code></code><translations></translations><inputs><input type="%clr">#000000</input></inputs></block-definition>
    <block-definition s="change pen %s by %n" type="command" category="pen" category-ru="Перо" description="Меняет параметры цвета пера (например, hue)"><header></header><code></code><translations></translations><inputs><input type="%s">hue</input><input type="%n">10</input></inputs></block-definition>
    <block-definition s="set pen %s to %n" type="command" category="pen" category-ru="Перо" description="Задаёт параметры цвета пера"><header></header><code></code><translations></translations><inputs><input type="%s">hue</input><input type="%n">0</input></inputs></block-definition>
    <block-definition s="pen %s" type="reporter" category="pen" category-ru="Перо" description="Возвращает параметр цвета пера"><header></header><code></code><translations></translations><inputs><input type="%s">hue</input></inputs></block-definition>
    <block-definition s="change pen size by %n" type="command" category="pen" category-ru="Перо" description="Меняет толщину пера"><header></header><code></code><translations></translations><inputs><input type="%n">1</input></inputs></block-definition>
    <block-definition s="set pen size to %n" type="command" category="pen" category-ru="Перо" description="Задаёт толщину пера"><header></header><code></code><translations></translations><inputs><input type="%n">5</input></inputs></block-definition>
    <block-definition s="stamp" type="command" category="pen" category-ru="Перо" description="Отпечатывает костюм спрайта"><header></header><code></code><translations></translations><inputs></inputs></block-definition>
    <block-definition s="fill" type="command" category="pen" category-ru="Перо" description="Заливает область цветом"><header></header><code></code><translations></translations><inputs></inputs></block-definition>
    <block-definition s="write %s size %n" type="command" category="pen" category-ru="Перо" description="Пишет текст на сцене"><header></header><code></code><translations></translations><inputs><input type="%s">Hello</input><input type="%n">20</input></inputs></block-definition>
    <block-definition s="pen trails" type="reporter" category="pen" category-ru="Перо" description="Возвращает нарисованное как картинку"><header></header><code></code><translations></translations><inputs></inputs></block-definition>
    <block-definition s="paste %s on %obj" type="command" category="pen" category-ru="Перо" description="Вставляет спрайт на костюм"><header></header><code></code><translations></translations><inputs><input type="%s">costume1</input><input type="%obj">Stage</input></inputs></block-definition>
    <block-definition s="cut from %obj" type="reporter" category="pen" category-ru="Перо" description="Вырезает из костюма"><header></header><code></code><translations></translations><inputs><input type="%obj">Stage</input></inputs></block-definition>
    <block-definition s="draw %s on %obj" type="command" category="pen" category-ru="Перо" description="Рисует на объекте (paint и т. п.)"><header></header><code></code><translations></translations><inputs><input type="%s">paint</input><input type="%obj">Stage</input></inputs></block-definition>
    <block-definition s="color %clr" type="reporter" category="pen" category-ru="Перо" description="Работает с цветом как с данными"><header></header><code></code><translations></translations><inputs><input type="%clr">#000000</input></inputs></block-definition>
    <block-definition s="%n of color %clr" type="reporter" category="pen" category-ru="Перо" description="Параметр цвета"><header></header><code></code><translations></translations><inputs><input type="%n">0</input><input type="%clr">#000000</input></inputs></block-definition>
    <block-definition s="new color %clr %clr %clr" type="reporter" category="pen" category-ru="Перо" description="Создаёт новый цвет"><header></header><code></code><translations></translations><inputs><input type="%clr">#FF0000</input><input type="%clr">#00FF00</input><input type="%clr">#0000FF</input></inputs></block-definition>
    <block-definition s="%clr = %clr" type="predicate" category="pen" category-ru="Перо" description="Сравнивает цвета"><header></header><code></code><translations></translations><inputs><input type="%clr">#000000</input><input type="%clr">#000000</input></inputs></block-definition>

    <!-- ==================== CONTROL (Управление) ==================== -->
    <block-definition s="when green flag clicked" type="hat" category="control" category-ru="Управление" description="Запуск по зелёному флагу"><header></header><code></code><translations></translations><inputs></inputs></block-definition>
    <block-definition s="when %s is edited" type="hat" category="control" category-ru="Управление" description="Срабатывает при правке значения"><header></header><code></code><translations></translations><inputs><input type="%s">variable</input></inputs></block-definition>
    <block-definition s="when I start as a clone" type="hat" category="control" category-ru="Управление" description="Запуск у нового клона"><header></header><code></code><translations></translations><inputs></inputs></block-definition>
    <block-definition s="when I receive %s" type="hat" category="control" category-ru="Управление" description="Запуск по сообщению"><header></header><code></code><translations></translations><inputs><input type="%s">message1</input></inputs></block-definition>
    <block-definition s="when %k key pressed" type="hat" category="control" category-ru="Управление" description="Запуск по нажатию клавиши"><header></header><code></code><translations></translations><inputs><input type="%k">space</input></inputs></block-definition>
    <block-definition s="when %b" type="hat" category="control" category-ru="Управление" description="Запуск по условию"><header></header><code></code><translations></translations><inputs><input type="%b">true</input></inputs></block-definition>
    <block-definition s="when I am %s" type="hat" category="control" category-ru="Управление" description="Запуск при взаимодействии (например, клик)"><header></header><code></code><translations></translations><inputs><input type="%s">clicked</input></inputs></block-definition>
    <block-definition s="broadcast %s" type="command" category="control" category-ru="Управление" description="Отправляет сообщение"><header></header><code></code><translations></translations><inputs><input type="%s">message1</input></inputs></block-definition>
    <block-definition s="broadcast %s and wait" type="command" category="control" category-ru="Управление" description="Отправляет сообщение и ждёт обработки"><header></header><code></code><translations></translations><inputs><input type="%s">message1</input></inputs></block-definition>
    <block-definition s="request %s" type="reporter" category="control" category-ru="Управление" description="Возвращает ответ на запрос"><header></header><code></code><translations></translations><inputs><input type="%s">message1</input></inputs></block-definition>
    <block-definition s="wait %n secs" type="command" category="control" category-ru="Управление" description="Ждёт время"><header></header><code></code><translations></translations><inputs><input type="%n">1</input></inputs></block-definition>
    <block-definition s="wait until %b" type="command" category="control" category-ru="Управление" description="Ждёт условие"><header></header><code></code><translations></translations><inputs><input type="%b">true</input></inputs></block-definition>
    <block-definition s="forever" type="c-command" category="control" category-ru="Управление" description="Цикл forever"><header></header><code></code><translations></translations><inputs></inputs></block-definition>
    <block-definition s="repeat %n" type="c-command" category="control" category-ru="Управление" description="Цикл repeat N"><header></header><code></code><translations></translations><inputs><input type="%n">10</input></inputs></block-definition>
    <block-definition s="repeat until %b" type="c-command" category="control" category-ru="Управление" description="Цикл repeat until"><header></header><code></code><translations></translations><inputs><input type="%b">true</input></inputs></block-definition>
    <block-definition s="for %u = %n to %n" type="c-command" category="control" category-ru="Управление" description="Цикл for i = N to M"><header></header><code></code><translations></translations><inputs><input type="%u">i</input><input type="%n">1</input><input type="%n">10</input></inputs></block-definition>
    <block-definition s="if %b then" type="c-command" category="control" category-ru="Управление" description="Ветвление if (команда)"><header></header><code></code><translations></translations><inputs><input type="%b">true</input></inputs></block-definition>
    <block-definition s="if %b then else" type="c-command" category="control" category-ru="Управление" description="Ветвление if-else (команда)"><header></header><code></code><translations></translations><inputs><input type="%b">true</input></inputs></block-definition>
    <block-definition s="if %b then %s else %s" type="reporter" category="control" category-ru="Управление" description="Ветвление if-else (reporter)"><header></header><code></code><translations></translations><inputs><input type="%b">true</input><input type="%s">yes</input><input type="%s">no</input></inputs></block-definition>
    <block-definition s="report %s" type="command" category="control" category-ru="Управление" description="Возвращает значение из блока"><header></header><code></code><translations></translations><inputs><input type="%s">value</input></inputs></block-definition>
    <block-definition s="stop %s" type="command" category="control" category-ru="Управление" description="Останавливает скрипт, все скрипты и т. д."><header></header><code></code><translations></translations><inputs><input type="%s">this script</input></inputs></block-definition>
    <block-definition s="run %ring" type="command" category="control" category-ru="Управление" description="Запускает функцию (ring), ждёт"><header></header><code></code><translations></translations><inputs><input type="%ring"></input></inputs></block-definition>
    <block-definition s="launch %ring" type="command" category="control" category-ru="Управление" description="Запускает функцию (ring) параллельно"><header></header><code></code><translations></translations><inputs><input type="%ring"></input></inputs></block-definition>
    <block-definition s="call %ring" type="reporter" category="control" category-ru="Управление" description="Вызывает функцию (ring), ждёт результат"><header></header><code></code><translations></translations><inputs><input type="%ring"></input></inputs></block-definition>
    <block-definition s="%ring ▶ %ring" type="reporter" category="control" category-ru="Управление" description="Передаёт значение по цепочке функций (pipe)"><header></header><code></code><translations></translations><inputs><input type="%ring"></input><input type="%ring"></input></inputs></block-definition>
    <block-definition s="tell %obj to %ring" type="command" category="control" category-ru="Управление" description="Заставляет другой объект выполнить функцию"><header></header><code></code><translations></translations><inputs><input type="%obj">Sprite1</input><input type="%ring"></input></inputs></block-definition>
    <block-definition s="ask %obj for %ring" type="reporter" category="control" category-ru="Управление" description="Заставляет другой объект вернуть значение функции"><header></header><code></code><translations></translations><inputs><input type="%obj">Sprite1</input><input type="%ring"></input></inputs></block-definition>
    <block-definition s="create a clone of %obj" type="command" category="control" category-ru="Управление" description="Создаёт клон"><header></header><code></code><translations></translations><inputs><input type="%obj">myself</input></inputs></block-definition>
    <block-definition s="a new clone of %obj" type="reporter" category="control" category-ru="Управление" description="Создаёт клон и возвращает его"><header></header><code></code><translations></translations><inputs><input type="%obj">myself</input></inputs></block-definition>
    <block-definition s="delete this clone" type="command" category="control" category-ru="Управление" description="Удаляет клон"><header></header><code></code><translations></translations><inputs></inputs></block-definition>
    <block-definition s="pause all" type="command" category="control" category-ru="Управление" description="Ставит выполнение на паузу"><header></header><code></code><translations></translations><inputs></inputs></block-definition>
    <block-definition s="switch to scene %s" type="command" category="control" category-ru="Управление" description="Переключает сцену"><header></header><code></code><translations></translations><inputs><input type="%s">Scene1</input></inputs></block-definition>
    <block-definition s="define %ring" type="command" category="control" category-ru="Управление" description="Создаёт пользовательский блок программно"><header></header><code></code><translations></translations><inputs><input type="%ring"></input></inputs></block-definition>
    <block-definition s="delete block %s" type="command" category="control" category-ru="Управление" description="Удаляет пользовательский блок"><header></header><code></code><translations></translations><inputs><input type="%s">block name</input></inputs></block-definition>
    <block-definition s="set %s of block %s to %s" type="command" category="control" category-ru="Управление" description="Меняет свойства блока"><header></header><code></code><translations></translations><inputs><input type="%s">label</input><input type="%s">block name</input><input type="%s">new label</input></inputs></block-definition>
    <block-definition s="%s of block %s" type="reporter" category="control" category-ru="Управление" description="Читает свойства блока"><header></header><code></code><translations></translations><inputs><input type="%s">label</input><input type="%s">block name</input></inputs></block-definition>
    <block-definition s="this %s" type="reporter" category="control" category-ru="Управление" description="Возвращает текущий скрипт или другой контекст"><header></header><code></code><translations></translations><inputs><input type="%s">script</input></inputs></block-definition>
    <block-definition s="set slot %n to %s" type="command" category="control" category-ru="Управление" description="Задаёт значение слота блока"><header></header><code></code><translations></translations><inputs><input type="%n">1</input><input type="%s">value</input></inputs></block-definition>

    <!-- ==================== SENSING (Сенсоры) ==================== -->
    <block-definition s="touching %obj ?" type="predicate" category="sensing" category-ru="Сенсоры" description="Касание объекта или цвета"><header></header><code></code><translations></translations><inputs><input type="%obj">mouse-pointer</input></inputs></block-definition>
    <block-definition s="color %clr is touching %clr ?" type="predicate" category="sensing" category-ru="Сенсоры" description="Касание одного цвета другим"><header></header><code></code><translations></translations><inputs><input type="%clr">#000000</input><input type="%clr">#FFFFFF</input></inputs></block-definition>
    <block-definition s="ask %s and wait" type="command" category="sensing" category-ru="Сенсоры" description="Задаёт вопрос пользователю и ждёт"><header></header><code></code><translations></translations><inputs><input type="%s">What's your name?</input></inputs></block-definition>
    <block-definition s="answer" type="reporter" category="sensing" category-ru="Сенсоры" description="Возвращает ответ пользователя"><header></header><code></code><translations></translations><inputs></inputs></block-definition>
    <block-definition s="mouse position" type="reporter" category="sensing" category-ru="Сенсоры" description="Данные мыши (позиция)"><header></header><code></code><translations></translations><inputs></inputs></block-definition>
    <block-definition s="mouse x" type="reporter" category="sensing" category-ru="Сенсоры" description="Координата X мыши"><header></header><code></code><translations></translations><inputs></inputs></block-definition>
    <block-definition s="mouse y" type="reporter" category="sensing" category-ru="Сенсоры" description="Координата Y мыши"><header></header><code></code><translations></translations><inputs></inputs></block-definition>
    <block-definition s="mouse down?" type="predicate" category="sensing" category-ru="Сенсоры" description="Нажата ли кнопка мыши"><header></header><code></code><translations></translations><inputs></inputs></block-definition>
    <block-definition s="key %k pressed?" type="predicate" category="sensing" category-ru="Сенсоры" description="Проверка клавиши"><header></header><code></code><translations></translations><inputs><input type="%k">space</input></inputs></block-definition>
    <block-definition s="%s to %obj" type="reporter" category="sensing" category-ru="Сенсоры" description="Отношение к объекту (например, расстояние)"><header></header><code></code><translations></translations><inputs><input type="%s">distance</input><input type="%obj">mouse-pointer</input></inputs></block-definition>
    <block-definition s="%s at %obj" type="reporter" category="sensing" category-ru="Сенсоры" description="Параметр в точке (например, цвет под курсором)"><header></header><code></code><translations></translations><inputs><input type="%s">color</input><input type="%obj">mouse-pointer</input></inputs></block-definition>
    <block-definition s="reset timer" type="command" category="sensing" category-ru="Сенсоры" description="Сбрасывает секундомер"><header></header><code></code><translations></translations><inputs></inputs></block-definition>
    <block-definition s="timer" type="reporter" category="sensing" category-ru="Сенсоры" description="Секундомер"><header></header><code></code><translations></translations><inputs></inputs></block-definition>
    <block-definition s="current %s" type="reporter" category="sensing" category-ru="Сенсоры" description="Текущая дата или время"><header></header><code></code><translations></translations><inputs><input type="%s">year</input></inputs></block-definition>
    <block-definition s="%s of %obj" type="reporter" category="sensing" category-ru="Сенсоры" description="Свойство другого спрайта"><header></header><code></code><translations></translations><inputs><input type="%s">x position</input><input type="%obj">Sprite1</input></inputs></block-definition>
    <block-definition s="my %s" type="reporter" category="sensing" category-ru="Сенсоры" description="Свойство самого спрайта (например, соседи)"><header></header><code></code><translations></translations><inputs><input type="%s">neighbors</input></inputs></block-definition>
    <block-definition s="object %s" type="reporter" category="sensing" category-ru="Сенсоры" description="Возвращает ссылку на объект"><header></header><code></code><translations></translations><inputs><input type="%s">Sprite1</input></inputs></block-definition>
    <block-definition s="url %s" type="reporter" category="sensing" category-ru="Сенсоры" description="Скачивает содержимое URL"><header></header><code></code><translations></translations><inputs><input type="%s">https://example.com</input></inputs></block-definition>
    <block-definition s="microphone %s" type="reporter" category="sensing" category-ru="Сенсоры" description="Данные с микрофона"><header></header><code></code><translations></translations><inputs><input type="%s">loudness</input></inputs></block-definition>
    <block-definition s="video %s on %obj" type="reporter" category="sensing" category-ru="Сенсоры" description="Данные с камеры"><header></header><code></code><translations></translations><inputs><input type="%s">motion</input><input type="%obj">Stage</input></inputs></block-definition>
    <block-definition s="set video transparency to %n %" type="command" category="sensing" category-ru="Сенсоры" description="Прозрачность видео"><header></header><code></code><translations></translations><inputs><input type="%n">50</input></inputs></block-definition>
    <block-definition s="is %s on?" type="predicate" category="sensing" category-ru="Сенсоры" description="Читает глобальные настройки (turbo mode, video capture)"><header></header><code></code><translations></translations><inputs><input type="%s">turbo mode</input></inputs></block-definition>
    <block-definition s="set %s to %b" type="command" category="sensing" category-ru="Сенсоры" description="Меняет глобальные настройки"><header></header><code></code><translations></translations><inputs><input type="%s">turbo mode</input><input type="%b">true</input></inputs></block-definition>

    <!-- ==================== OPERATORS (Операторы) ==================== -->
    <block-definition s="%n + %n" type="reporter" category="operators" category-ru="Операторы" description="Сложение"><header></header><code></code><translations></translations><inputs><input type="%n">0</input><input type="%n">0</input></inputs></block-definition>
    <block-definition s="%n - %n" type="reporter" category="operators" category-ru="Операторы" description="Вычитание"><header></header><code></code><translations></translations><inputs><input type="%n">0</input><input type="%n">0</input></inputs></block-definition>
    <block-definition s="%n × %n" type="reporter" category="operators" category-ru="Операторы" description="Умножение"><header></header><code></code><translations></translations><inputs><input type="%n">0</input><input type="%n">0</input></inputs></block-definition>
    <block-definition s="%n ÷ %n" type="reporter" category="operators" category-ru="Операторы" description="Деление"><header></header><code></code><translations></translations><inputs><input type="%n">0</input><input type="%n">1</input></inputs></block-definition>
    <block-definition s="%n ^ %n" type="reporter" category="operators" category-ru="Операторы" description="Возведение в степень"><header></header><code></code><translations></translations><inputs><input type="%n">0</input><input type="%n">0</input></inputs></block-definition>
    <block-definition s="%n mod %n" type="reporter" category="operators" category-ru="Операторы" description="Остаток от деления"><header></header><code></code><translations></translations><inputs><input type="%n">0</input><input type="%n">1</input></inputs></block-definition>
    <block-definition s="min %n %n" type="reporter" category="operators" category-ru="Операторы" description="Минимум"><header></header><code></code><translations></translations><inputs><input type="%n">0</input><input type="%n">0</input></inputs></block-definition>
    <block-definition s="max %n %n" type="reporter" category="operators" category-ru="Операторы" description="Максимум"><header></header><code></code><translations></translations><inputs><input type="%n">0</input><input type="%n">0</input></inputs></block-definition>
    <block-definition s="round %n" type="reporter" category="operators" category-ru="Операторы" description="Округление"><header></header><code></code><translations></translations><inputs><input type="%n">0</input></inputs></block-definition>
    <block-definition s="%s of %n" type="reporter" category="operators" category-ru="Операторы" description="Математические функции (sqrt и др.)"><header></header><code></code><translations></translations><inputs><input type="%s">sqrt</input><input type="%n">0</input></inputs></block-definition>
    <block-definition s="atan2 %n %n" type="reporter" category="operators" category-ru="Операторы" description="Арктангенс двух аргументов"><header></header><code></code><translations></translations><inputs><input type="%n">0</input><input type="%n">0</input></inputs></block-definition>
    <block-definition s="pick random %n to %n" type="reporter" category="operators" category-ru="Операторы" description="Случайное число"><header></header><code></code><translations></translations><inputs><input type="%n">1</input><input type="%n">10</input></inputs></block-definition>
    <block-definition s="%n &lt; %n" type="predicate" category="operators" category-ru="Операторы" description="Меньше"><header></header><code></code><translations></translations><inputs><input type="%n">0</input><input type="%n">0</input></inputs></block-definition>
    <block-definition s="%n = %n" type="predicate" category="operators" category-ru="Операторы" description="Равно"><header></header><code></code><translations></translations><inputs><input type="%n">0</input><input type="%n">0</input></inputs></block-definition>
    <block-definition s="%n &gt; %n" type="predicate" category="operators" category-ru="Операторы" description="Больше"><header></header><code></code><translations></translations><inputs><input type="%n">0</input><input type="%n">0</input></inputs></block-definition>
    <block-definition s="%b and %b" type="predicate" category="operators" category-ru="Операторы" description="Логическое И"><header></header><code></code><translations></translations><inputs><input type="%b">true</input><input type="%b">true</input></inputs></block-definition>
    <block-definition s="%b or %b" type="predicate" category="operators" category-ru="Операторы" description="Логическое ИЛИ"><header></header><code></code><translations></translations><inputs><input type="%b">true</input><input type="%b">true</input></inputs></block-definition>
    <block-definition s="not %b" type="predicate" category="operators" category-ru="Операторы" description="Логическое НЕ"><header></header><code></code><translations></translations><inputs><input type="%b">true</input></inputs></block-definition>
    <block-definition s="true-false %b" type="reporter" category="operators" category-ru="Операторы" description="Преобразование булева в число"><header></header><code></code><translations></translations><inputs><input type="%b">true</input></inputs></block-definition>
    <block-definition s="join %s %s" type="reporter" category="operators" category-ru="Операторы" description="Склеивание текста"><header></header><code></code><translations></translations><inputs><input type="%s">Hello</input><input type="%s">World</input></inputs></block-definition>
    <block-definition s="split %s at %s" type="reporter" category="operators" category-ru="Операторы" description="Разбиение текста"><header></header><code></code><translations></translations><inputs><input type="%s">Hello,World</input><input type="%s">,</input></inputs></block-definition>
    <block-definition s="letter %n of %s" type="reporter" category="operators" category-ru="Операторы" description="Буква по номеру"><header></header><code></code><translations></translations><inputs><input type="%n">1</input><input type="%s">Hello</input></inputs></block-definition>
    <block-definition s="%s of text %s" type="reporter" category="operators" category-ru="Операторы" description="Свойства текста (например, длина)"><header></header><code></code><translations></translations><inputs><input type="%s">length</input><input type="%s">Hello</input></inputs></block-definition>
    <block-definition s="unicode of %s" type="reporter" category="operators" category-ru="Операторы" description="Перевод символа в код"><header></header><code></code><translations></translations><inputs><input type="%s">A</input></inputs></block-definition>
    <block-definition s="unicode %n as letter" type="reporter" category="operators" category-ru="Операторы" description="Перевод кода в символ"><header></header><code></code><translations></translations><inputs><input type="%n">65</input></inputs></block-definition>
    <block-definition s="is %s a %s ?" type="predicate" category="operators" category-ru="Операторы" description="Проверка типа значения"><header></header><code></code><translations></translations><inputs><input type="%s">value</input><input type="%s">number</input></inputs></block-definition>
    <block-definition s="is %s identical to %s ?" type="predicate" category="operators" category-ru="Операторы" description="Проверка тождественности объектов"><header></header><code></code><translations></translations><inputs><input type="%s">a</input><input type="%s">b</input></inputs></block-definition>

    <!-- ==================== VARIABLES (Переменные) ==================== -->
    <block-definition s="set %v to %s" type="command" category="variables" category-ru="Переменные" description="Присваивает значение"><header></header><code></code><translations></translations><inputs><input type="%v">variable</input><input type="%s">value</input></inputs></block-definition>
    <block-definition s="change %v by %n" type="command" category="variables" category-ru="Переменные" description="Увеличивает значение"><header></header><code></code><translations></translations><inputs><input type="%v">variable</input><input type="%n">1</input></inputs></block-definition>
    <block-definition s="show variable %v" type="command" category="variables" category-ru="Переменные" description="Показывает переменную на сцене"><header></header><code></code><translations></translations><inputs><input type="%v">variable</input></inputs></block-definition>
    <block-definition s="hide variable %v" type="command" category="variables" category-ru="Переменные" description="Скрывает переменную на сцене"><header></header><code></code><translations></translations><inputs><input type="%v">variable</input></inputs></block-definition>
    <block-definition s="inherit %v" type="reporter" category="variables" category-ru="Переменные" description="Возвращает клону наследование значения от оригинала"><header></header><code></code><translations></translations><inputs><input type="%v">variable</input></inputs></block-definition>

    <!-- ==================== LISTS (Списки) ==================== -->
    <block-definition s="list %s" type="reporter" category="lists" category-ru="Списки" description="Создаёт список из одного элемента"><header></header><code></code><translations></translations><inputs><input type="%s">item</input></inputs></block-definition>
    <block-definition s="numbers from %n to %n" type="reporter" category="lists" category-ru="Списки" description="Последовательность чисел"><header></header><code></code><translations></translations><inputs><input type="%n">1</input><input type="%n">10</input></inputs></block-definition>
    <block-definition s="%s in front of %l" type="reporter" category="lists" category-ru="Списки" description="Добавляет элемент в начало"><header></header><code></code><translations></translations><inputs><input type="%s">item</input><input type="%l"></input></inputs></block-definition>
    <block-definition s="item %n of %l" type="reporter" category="lists" category-ru="Списки" description="Элемент по индексу"><header></header><code></code><translations></translations><inputs><input type="%n">1</input><input type="%l"></input></inputs></block-definition>
    <block-definition s="all but first of %l" type="reporter" category="lists" category-ru="Списки" description="Список без первого элемента"><header></header><code></code><translations></translations><inputs><input type="%l"></input></inputs></block-definition>
    <block-definition s="%s of %l" type="reporter" category="lists" category-ru="Списки" description="Свойства списка (length и др.)"><header></header><code></code><translations></translations><inputs><input type="%s">length</input><input type="%l"></input></inputs></block-definition>
    <block-definition s="index of %s in %l" type="reporter" category="lists" category-ru="Списки" description="Индекс элемента"><header></header><code></code><translations></translations><inputs><input type="%s">item</input><input type="%l"></input></inputs></block-definition>
    <block-definition s="%l contains %s ?" type="predicate" category="lists" category-ru="Списки" description="Проверка наличия"><header></header><code></code><translations></translations><inputs><input type="%l"></input><input type="%s">item</input></inputs></block-definition>
    <block-definition s="is %l empty?" type="predicate" category="lists" category-ru="Списки" description="Проверка на пустоту"><header></header><code></code><translations></translations><inputs><input type="%l"></input></inputs></block-definition>
    <block-definition s="map %ring over %l" type="reporter" category="lists" category-ru="Списки" description="Функция высшего порядка: преобразовать"><header></header><code></code><translations></translations><inputs><input type="%ring"></input><input type="%l"></input></inputs></block-definition>
    <block-definition s="keep %b from %l" type="reporter" category="lists" category-ru="Списки" description="Функция высшего порядка: отфильтровать"><header></header><code></code><translations></translations><inputs><input type="%b">true</input><input type="%l"></input></inputs></block-definition>
    <block-definition s="find first %s in %l" type="reporter" category="lists" category-ru="Списки" description="Функция высшего порядка: найти"><header></header><code></code><translations></translations><inputs><input type="%s">item</input><input type="%l"></input></inputs></block-definition>
    <block-definition s="combine %l using %ring" type="reporter" category="lists" category-ru="Списки" description="Функция высшего порядка: свернуть"><header></header><code></code><translations></translations><inputs><input type="%l"></input><input type="%ring"></input></inputs></block-definition>
    <block-definition s="for each %u in %l" type="c-command" category="lists" category-ru="Списки" description="Цикл по элементам"><header></header><code></code><translations></translations><inputs><input type="%u">i</input><input type="%l"></input></inputs></block-definition>
    <block-definition s="add %s to %l" type="command" category="lists" category-ru="Списки" description="Добавляет элемент в конец"><header></header><code></code><translations></translations><inputs><input type="%s">item</input><input type="%l"></input></inputs></block-definition>
    <block-definition s="delete %n of %l" type="command" category="lists" category-ru="Списки" description="Удаляет элемент по индексу"><header></header><code></code><translations></translations><inputs><input type="%n">1</input><input type="%l"></input></inputs></block-definition>
    <block-definition s="insert %s at %n of %l" type="command" category="lists" category-ru="Списки" description="Вставляет элемент по индексу"><header></header><code></code><translations></translations><inputs><input type="%s">item</input><input type="%n">1</input><input type="%l"></input></inputs></block-definition>
    <block-definition s="replace item %n of %l with %s" type="command" category="lists" category-ru="Списки" description="Заменяет элемент по индексу"><header></header><code></code><translations></translations><inputs><input type="%n">1</input><input type="%l"></input><input type="%s">new item</input></inputs></block-definition>
    <block-definition s="append %l %l" type="reporter" category="lists" category-ru="Списки" description="Склеивает списки"><header></header><code></code><translations></translations><inputs><input type="%l"></input><input type="%l"></input></inputs></block-definition>
    <block-definition s="reshape %l to %n" type="reporter" category="lists" category-ru="Списки" description="Меняет форму списка (многомерные массивы)"><header></header><code></code><translations></translations><inputs><input type="%l"></input><input type="%n">2</input></inputs></block-definition>
    <block-definition s="combinations of %l" type="reporter" category="lists" category-ru="Списки" description="Все комбинации элементов"><header></header><code></code><translations></translations><inputs><input type="%l"></input></inputs></block-definition>

    </blocks>






    вот концептуальнаая идея 


    # Проект: язык программирования для Snap с генерацией через ИИ

    ## 1. Идея проекта

    Мне нужно выполнить проект в Snap, однако я не хочу программировать непосредственно в визуальном интерфейсе Snap. Вместо этого я хочу использовать ИИ для генерации программ в текстовом формате — методом вайбкодинга.

    Основная проблема заключается в том, что Snap использует визуальное программирование через собственный пользовательский интерфейс. Проекты Snap можно изменять, скачивая XML-файл и редактируя его вручную или программно.

    Однако XML-файлы Snap могут содержать десятки тысяч строк. Поэтому ИИ не всегда способен надёжно создавать или редактировать такие файлы целиком. Пример небольшого XML-проекта прилагается только для демонстрации структуры и размера файла. Сам файл анализировать не требуется.

    ## 2. Главная цель

    Нужно создать промежуточный язык программирования, который позволит:

    1. Генерировать код с помощью ИИ.
    2. Писать программы в простом текстовом формате.
    3. Переводить этот текстовый код в XML-структуру, совместимую с Snap.
    4. Запускать получившийся XML-проект в Snap.

    Иными словами, проект должен работать как компилятор или транслятор из собственного текстового языка в XML Snap.

    ## 3. Почему такой подход может работать

    Визуальные блоки Snap можно описывать обычным текстом.

    Например, последовательность блоков может означать следующее:

    - после запуска проекта выполняется цикл;
    - объект перемещается;
    - воспроизводится звук;
    - изменяется значение переменной.

    У подобных действий есть аналоги в обычных языках программирования, например в Python. Если необходимой операции нет, её можно описать в собственном языке и затем связать с соответствующим блоком Snap.

    Следовательно, Snap можно рассматривать как систему команд, где каждая визуальная конструкция имеет текстовое представление.

    Проблема заключается в том, что ИИ не должен напрямую работать с большим и сложным XML-файлом. Поэтому необходима отдельная программа-переходник:

    ```text
    Код, сгенерированный ИИ
            ↓
    Промежуточный язык
            ↓
    Транслятор
            ↓
    XML-файл Snap
            ↓
    Запуск проекта в Snap
    ```

    ## 4. Собственный язык программирования

    Предлагается создать максимально простой язык без лишних конструкций и сложного синтаксиса.

    В качестве основы можно использовать синтаксис Python, потому что он:

    - легко читается;
    - не требует большого количества специальных символов;
    - хорошо объясняется нейросетям;
    - позволяет удобно описывать последовательность действий;
    - подходит для процедурного преобразования в XML.

    !!! мы не используем питон мы всего лишь юзаем его синтаксис тк это проще чем придумывать свой у нас будет свое расширение отличное от .py 

    Главное требование — язык должен быть простым для человека и ИИ, а также однозначно переводиться в блоки Snap.

    ## 5. Пример синтаксиса

    ```text
    sprite Cat:

    when_green_flag:
        set("score", 0)
        goto(0, 0)

    repeat 10:
        move(10)
        play_sound("Meow")
        change("score", 1)

    when_key("space"):
        say("Прыжок!", 1)
        change_y(30)
    ```

    Этот код описывает спрайт `Cat` и несколько сценариев его поведения.

    ### 5.1. Сценарий запуска

    ```text
    when_green_flag:
        set("score", 0)
        goto(0, 0)
    ```

    После нажатия на зелёный флаг:

    1. Переменная `score` устанавливается в значение `0`.
    2. Спрайт перемещается в координаты `(0, 0)`.

    ### 5.2. Цикл

    ```text
    repeat 10:
        move(10)
        play_sound("Meow")
        change("score", 1)
    ```

    Цикл выполняется 10 раз. На каждой итерации:

    1. Спрайт перемещается на 10 шагов.
    2. Воспроизводится звук `Meow`.
    3. Значение переменной `score` увеличивается на 1.

    ### 5.3. Обработка нажатия клавиши

    ```text
    when_key("space"):
        say("Прыжок!", 1)
        change_y(30)
    ```

    При нажатии клавиши `space`:

    1. Спрайт говорит `Прыжок!` в течение 1 секунды.
    2. Координата по оси Y увеличивается на 30.

    ## 6. Что должно входить в проект

    Проект должен состоять из трёх основных частей.

    ### 6.1. Язык программирования

    Необходимо определить:

    - синтаксис языка;
    - правила отступов;
    - поддерживаемые типы данных;
    - переменные;
    - арифметические операции;
    - логические выражения;
    - условия;
    - циклы;
    - процедуры или пользовательские блоки;
    - обработчики событий;
    - команды управления спрайтами;
    - команды работы со звуком и внешним видом;
    - правила обработки ошибок.

    ### 6.2. Инструкция для ИИ

    Нужно создать подробную инструкцию, объясняющую нейросети, как писать программы на этом языке.

    Инструкция должна описывать:

    - назначение языка;
    - допустимый синтаксис;
    - структуру файла;
    - каждый доступный блок или оператор;
    - параметры каждой команды;
    - типы аргументов;
    - правила вложенности;
    - доступные события;
    - правила именования переменных и спрайтов;
    - примеры правильного кода;
    - примеры неправильного кода;
    - формат сообщений об ошибках;
    - ограничения языка;
    - правила, запрещающие ИИ использовать неподдерживаемые конструкции.

    Инструкция должна быть написана так, чтобы ИИ мог стабильно генерировать валидный код без необходимости создавать XML вручную.

    ### 6.3. Транслятор в XML Snap

    Нужно написать программу на Python или Java, которая будет:

    1. Читать файл с кодом собственного языка.
    2. Проверять его синтаксис.
    3. Создавать внутреннее представление программы.
    4. Преобразовывать команды в соответствующие блоки Snap.
    5. Формировать XML-файл проекта.
    6. Сохранять XML в формате, который сможет открыть Snap.
    7. Показывать понятные ошибки при неправильном коде.

    Рекомендуемый вариант реализации — Python, поскольку он подходит для быстрой разработки парсера и транслятора.

    ## 7. Предлагаемая архитектура

    ```text
    Файл исходного кода
            ↓
    Лексический анализатор
            ↓
    Синтаксический анализатор
            ↓
    AST или другое внутреннее представление
            ↓
    Проверка типов и семантики
            ↓
    Генератор блоков Snap
            ↓
    Генератор XML
            ↓
    Готовый проект Snap
    ```

    ### 7.1. Лексический анализатор

    Лексический анализатор разбивает исходный код на элементы:

    - ключевые слова;
    - имена спрайтов;
    - имена команд;
    - числа;
    - строки;
    - скобки;
    - запятые;
    - двоеточия;
    - отступы.

    ### 7.2. Синтаксический анализатор

    Синтаксический анализатор проверяет, соответствует ли код грамматике языка.

    Например, он должен определить:

    - где начинается спрайт;
    - где начинается обработчик события;
    - какие команды относятся к обработчику;
    - где начинается и заканчивается цикл;
    - правильно ли указаны аргументы команд.

    ### 7.3. Внутреннее представление

    После разбора исходного кода программу желательно представить в виде AST — абстрактного синтаксического дерева.

    Примерная структура:

    ```text
    Program
    └── Sprite(Cat)
        ├── Event(when_green_flag)
        │   ├── SetVariable(score, 0)
        │   └── Goto(0, 0)
        ├── Repeat(10)
        │   ├── Move(10)
        │   ├── PlaySound(Meow)
        │   └── ChangeVariable(score, 1)
        └── Event(when_key, space)
            ├── Say(Прыжок!, 1)
            └── ChangeY(30)
    ```

    Использование AST позволит отделить анализ языка от генерации XML. Это упростит расширение проекта и обработку ошибок.

    ## 8. Таблица соответствий команд

    Транслятор должен иметь таблицу, связывающую команды собственного языка с блоками Snap.

    | Команда языка | Назначение | Блок Snap |
    |---|---|---|
    | `set(name, value)` | Установить значение переменной | `setVar` |
    | `change(name, value)` | Изменить значение переменной | `changeVar` |
    | `goto(x, y)` | Перейти в координаты | `gotoXY` |
    | `move(steps)` | Переместить спрайт | `forward` или аналогичный блок движения |
    | `play_sound(name)` | Воспроизвести звук | `doPlaySound` |
    | `say(text, seconds)` | Показать сообщение | `bubble` или аналогичный блок речи |
    | `change_y(value)` | Изменить координату Y | `changeYpos` |
    | `repeat(count)` | Повторить последовательность команд | `doRepeat` |
    | `when_green_flag` | Обработчик запуска | блок запуска по зелёному флагу |
    | `when_key(key)` | Обработчик нажатия клавиши | блок события клавиши |

    Точные названия Snap-блоков необходимо проверить по XML-файлу, документации Snap или экспериментально в самом редакторе. Нельзя полагаться только на предположительные названия.

    ## 9. Важная техническая проблема: формат XML Snap

    Основная сложность проекта состоит не в создании текстового языка, а в корректной генерации XML, который Snap сможет открыть и выполнить.

    Необходимо исследовать:

    - структуру XML-файла Snap;
    - формат описания спрайтов;
    - формат описания блоков;
    - связи между блоками;
    - порядок и вложенность блоков;
    - представление переменных;
    - представление списков;
    - представление костюмов и звуков;
    - координаты блоков на рабочем поле;
    - формат пользовательских блоков;
    - правила экранирования XML-символов;
    - обязательные атрибуты и узлы;
    - совместимость разных версий Snap.

    Нельзя просто создавать XML с произвольными именами блоков. Генератор должен использовать фактическую структуру, которую Snap принимает.

    ## 10. Рекомендуемый план разработки

    ### Этап 1. Исследование XML

    1. Создать в Snap минимальный проект.
    2. Добавить один блок запуска.
    3. Сохранить проект как XML.
    4. Изучить структуру файла.
    5. Добавить одну команду движения.
    6. Снова сохранить проект.
    7. Сравнить два XML-файла.
    8. Определить, какие узлы соответствуют каждому блоку.

    ### Этап 2. Минимальный язык

    Сначала поддержать только несколько команд:

    - `sprite`;
    - `when_green_flag`;
    - `move`;
    - `goto`;
    - `set`;
    - `change`;
    - `repeat`.

    Не следует сразу реализовывать все возможности Snap.

    ### Этап 3. Парсер

    Реализовать разбор простого кода и преобразование его в AST.

    На этом этапе генерация XML ещё может отсутствовать. Важно сначала добиться корректного разбора исходного языка.

    ### Этап 4. Генератор XML

    Добавить преобразование AST в XML-блоки Snap.

    Генератор должен создавать XML через библиотеку, например:

    - `xml.etree.ElementTree` в Python;
    - DOM API в Java.

    Не рекомендуется собирать XML обычной конкатенацией строк, поскольку это повышает риск ошибок с экранированием и вложенностью элементов.

    ### Этап 5. Проверка результата

    Для каждого теста необходимо:

    1. Создать исходный код на собственном языке.
    2. Сгенерировать XML.
    3. Открыть XML в Snap.
    4. Проверить структуру проекта.
    5. Запустить проект.
    6. Сравнить фактическое поведение с ожидаемым.

    ### Этап 6. Расширение языка

    После успешной реализации минимального набора постепенно добавить:

    - условия;
    - циклы `while`;
    - пользовательские процедуры;
    - сообщения;
    - переменные для всех спрайтов;
    - локальные переменные;
    - списки;
    - операторы сравнения;
    - математические операции;
    - логические операции;
    - клоны;
    - костюмы;
    - звуки;
    - отправку и обработку сообщений.

    ## 11. Возможные варианты реализации

    ### Вариант A: прямой транслятор

    ```text
    Собственный язык → XML Snap
    ```

    Преимущества:

    - проще архитектура;
    - меньше промежуточных компонентов;
    - быстрее создать первый прототип.

    Недостатки:

    - сложнее поддерживать большое количество команд;
    - генератор будет напрямую зависеть от формата XML Snap.

    ### Вариант B: язык → AST → промежуточная модель → XML

    ```text
    Собственный язык → AST → модель блоков Snap → XML
    ```

    Преимущества:

    - проще тестировать отдельные этапы;
    - удобнее добавлять новые команды;
    - можно заменить XML-генератор;
    - проще анализировать ошибки.

    Недостатки:

    - больше кода;
    - сложнее первоначальная архитектура.

    Для полноценного проекта предпочтителен вариант B.

    ## 12. Ограничения проекта

    Нужно учитывать следующие ограничения:

    - ИИ не должен генерировать XML напрямую.
    - ИИ должен использовать только команды, описанные в спецификации языка.
    - Каждая команда должна иметь однозначное соответствие блоку Snap.
    - Неподдерживаемые функции Snap должны явно отмечаться как недоступные.
    - Формат XML может зависеть от версии Snap.
    - Необходимо проверять корректность XML после генерации.
    - Нельзя считать, что названия блоков Snap совпадают с названиями функций собственного языка.
    - Большие программы всё равно могут быть сложными, поэтому язык должен поддерживать разбиение проекта на файлы или модули.

    ## 13. Возможное расширение: модульная структура

    Чтобы не создавать слишком большие файлы, проект можно разделить на несколько файлов:

    ```text
    project/
    ├── project.snapcode
    ├── sprites/
    │   ├── cat.snapcode
    │   └── player.snapcode
    ├── variables.snapcode
    ├── sounds.snapcode
    └── assets/
    ```

    Транслятор сможет объединять эти файлы в один XML-проект Snap.

    Это уменьшит размер отдельных файлов и позволит ИИ работать с небольшими частями проекта.

    ## 14. Требования к инструкции для нейросети

    Инструкция для ИИ должна содержать строгие правила:

    1. Всегда использовать только команды из спецификации.
    2. Не генерировать XML.
    3. Не использовать Python-функции, если они не определены в языке.
    4. Не добавлять произвольные параметры.
    5. Соблюдать отступы.
    6. Использовать один стиль кавычек.
    7. Не смешивать синтаксис нескольких языков.
    8. При необходимости создавать несколько небольших файлов.
    9. Перед выводом проверять количество аргументов каждой команды.
    10. Не использовать неподдерживаемые функции без явного сообщения об этом.

    ## 15. Пример промпта для ИИ

    ```text
    Ты пишешь программы на языке SnapCode.

    Используй только синтаксис и команды, описанные в спецификации.
    Не создавай XML и не используй команды Snap напрямую.
    Не добавляй неподдерживаемые конструкции.
    Соблюдай отступы в 4 пробела.

    Каждая программа должна начинаться с объявления спрайта:

    sprite Имя:

    Обработчики событий и команды должны быть вложены с отступом.

    Если задача не может быть решена с помощью доступных команд, напиши:
    UNSUPPORTED: описание недоступной возможности

    Перед выводом проверь:
    - все команды существуют;
    - количество аргументов корректно;
    - строки заключены в кавычки;
    - отступы соблюдены;
    - циклы и обработчики имеют правильную вложенность.
    ```

    ## 16. Минимальный MVP

    Минимальная рабочая версия проекта должна уметь:

    - читать один текстовый файл;
    - распознавать один спрайт;
    - распознавать обработчик зелёного флага;
    - распознавать команды движения;
    - распознавать переменные;
    - распознавать цикл `repeat`;
    - строить внутреннее представление программы;
    - генерировать XML;
    - создавать файл, который открывается в Snap;
    - сообщать об ошибках синтаксиса.

    Пример минимальной программы:

    ```text
    sprite Cat:

    when_green_flag:
        move(10)
    ```

    Если этот пример корректно преобразуется в XML и запускается в Snap, можно переходить к более сложным конструкциям.

    ## 17. Главные вопросы, которые нужно решить

    1. Как точно устроен XML-формат Snap?
    2. Какие XML-узлы соответствуют конкретным блокам?
    3. Как Snap хранит вложенные блоки и циклы?
    4. Как Snap хранит события?
    5. Как объявляются и изменяются переменные?
    6. Как кодировать строки и специальные символы?
    7. Как поддерживать несколько спрайтов?
    8. Как добавлять звуки и костюмы?
    9. Как обрабатывать пользовательские блоки?
    10. Как проверять XML до открытия в Snap?
    11. Нужно ли поддерживать несколько файлов исходного кода?
    12. Как обеспечить совместимость с конкретной версией Snap?

    ## 18. Итоговая формулировка задачи

    Необходимо разработать интерпретируемый или транслируемый текстовый язык для создания проектов Snap с помощью ИИ.

    Проект должен включать:

    1. Простый язык программирования на основе Python или собственного минимального синтаксиса.
    2. Формальную спецификацию языка.
    3. Инструкцию для нейросети по написанию программ на этом языке.
    4. Парсер исходного кода.
    5. Внутреннее представление программы, желательно AST.
    6. Проверку синтаксиса и семантики.
    7. Транслятор на Python или Java.
    8. Генератор XML-файлов Snap.
    9. Систему понятных сообщений об ошибках.
    10. Набор тестовых программ.
    11. Документацию по соответствию команд языка блокам Snap.

    Основная идея проекта:

    ```

## 18. Итоговая формулировка задачи

Необходимо разработать язык SnapCode для создания проектов Snap! с помощью человека и ИИ.

Целевая среда — модифицированный Snap! 12.2.0 offline. Компилятор и декомпилятор выполняются на JavaScript непосредственно внутри Snap!.

Проект включает:

1. Формальную спецификацию SnapCode.
2. Нормативную грамматику языка.
3. Инструкцию для ИИ.
4. JavaScript lexer и parser.
5. AST с исходными диапазонами позиций.
6. Проверку имён, типов и областей видимости.
7. Snap IR, независимый от XML.
8. XML adapter для Snap! 12.2.0.
9. Декомпилятор XML → SnapCode.
10. Систему диагностических сообщений.
11. Встроенный редактор SnapCode.
12. Node.js CLI для разработки и тестирования.
13. Набор unit-, golden-, round-trip- и conformance-тестов.
14. Ограничения безопасности для XML, путей и ресурсов.

Основная цепочка:

```text
ИИ генерирует SnapCode
        ↓
JavaScript parser строит AST
        ↓
Semantic analyzer проверяет программу
        ↓
Lowering строит Snap IR
        ↓
XML adapter создаёт XML Snap!
        ↓
Snap! загружает и выполняет проект
```

Обратная цепочка:

```text
XML-проект Snap!
        ↓
Snap IR
        ↓
AST
        ↓
SnapCode formatter
```

Python и Java не являются языками runtime-реализации. Node.js используется только для CLI и инструментов разработки.

---


    ## 19. встроенный редактор

    я скачал исходник snap и хочу в него встроить редактор нашего кода это должно быть окошко подобное окну ассистента в comet я хочу там просто редактировать код надать на кнопку и он алгоритмом пересобирется в xml и просто загрузится 

    также из логики должна быть логика что если мы открываем просто проект snap то должна быть обратная декомпиляция из xml в наш язык 

    ---

    # Часть 2. Спецификация SnapCode и интеграции со Snap!

    # SnapCode: спецификация языка и интеграции со Snap! 12.2.0

    > Статус: утверждённая техническая спецификация версии 1.0.  
    > Целевая платформа: Snap! 12.2.0, официальный тег `v12.2.0`.  
    > Исходные файлы: `.snapcode`.  
    > Реализация транслятора: Java.  
    > Охват: полная модель проекта Snap!, включая неизвестные и будущие конструкции через обратимые низкоуровневые формы.  
    > Интерфейс: кнопка на правой границе Snap! и выдвижное окно редактора в стиле панели ассистента Comet, но без чата.

    ## 1. Назначение

    SnapCode — текстовый язык и набор инструментов для создания, изменения и обратной декомпиляции проектов Snap!. Пользователь или ИИ пишет компактный `.snapcode`, Java-транслятор строит типизированную промежуточную модель, создаёт XML Snap! 12.2.0 и передаёт его в открытый редактор Snap!. При загрузке обычного проекта Snap! выполняется обратное преобразование XML в SnapCode.

    Snap! является блочным языком с пользовательскими блоками, первоклассными списками, процедурами, спрайтами, костюмами, звуками и продолжениями; поэтому полное покрытие нельзя свести к небольшому набору команд наподобие `move` и `say`.[cite:20][cite:22] Полнота SnapCode достигается двумя уровнями: удобным синтаксисом для повседневных конструкций и каноническим синтаксисом `primitive`, `custom` и `raw_*`, способным выразить каждый сериализуемый элемент проекта.

    ## 2. Принятые решения

    | Вопрос | Решение |
    |---|---|
    | Целевая версия | Только Snap! 12.2.0; адаптер версии закреплён за тегом `v12.2.0`.[cite:33] |
    | Охват | Полное покрытие Snap!, а не ограниченный MVP. |
    | Текущий документ | Полностью перестроен; прежние повторы и предположительные XML-описания удалены. |
    | Язык реализации | Java, минимальная версия выполнения Java 21. |
    | Расширение | `.snapcode`. |
    | Неизвестные блоки | Сохраняются через `raw_block`, `raw_value` и `raw_xml`; данные не отбрасываются. |
    | Интерфейс | Круглая кнопка и выдвижная правая панель с редактором кода, не чат. |
    | Текущий этап | Только спецификация; реализация не входит в эту редакцию. |

    ## 3. Границы полноты

    «Полное покрытие» означает следующее:

    - Каждый примитив Snap! 12.2.0 представим по его внутреннему selector, а не по переведённой надписи на блоке.
    - Представимы команды, репортёры, предикаты, шляпы, кольца, C-блоки и вложенные скрипты.
    - Представимы сцены, сцена-Stage, спрайты, переменные всех областей, списки, наблюдатели, костюмы, звуки, перьевой слой, настройки проекта, наследование, клоны в программной логике, пользовательские категории и пользовательские блоки.
    - Представимы первоклассные скрипты и процедуры: Snap! использует `run` и `call`, а также умеет разбирать и собирать синтаксические деревья программ.[cite:92][cite:97]
    - Всё, что адаптер распознал, получает типизированную модель; всё неизвестное сохраняется как непрозрачный XML-фрагмент с указанием позиции.
    - Полнота относится к сериализуемому проекту. Мгновенное состояние выполнения — активные потоки, стек вызовов, временные клоны, проигрываемый звук и состояние камеры — не обязано восстанавливаться, если сам Snap! не экспортирует его в проект.

    В Snap! 12.2.0 реестр исходного кода содержит 256 записей примитивов в десяти категориях, включая 30 записей режима разработчика. Этот реестр, а не вручную написанный список, является источником таблицы selector-ов в приложении A.[cite:19] Официальная документация также публикует сводную таблицу блоков, их типов, категорий и текстовых форм.[cite:95]

    ## 4. Архитектура

    ```text
    ┌──────────────────────────── Snap! 12.2.0 fork ────────────────────────────┐
    │ Кнопка SnapCode → правая панель → редактор → диагностика → preview       │
    │        │                                      │                           │
    │        └──────────── HTTP localhost + token ──┘                           │
    └──────────────────────────────────┬────────────────────────────────────────┘
                                    │
    ┌──────────────────────── Java service/CLI ─────────────────────────────────┐
    │ Lexer → Parser → AST → Semantic model → Snap IR → XML adapter 12.2.0      │
    │ XML 12.2.0 → Snap IR → Normalizer → Pretty-printer → .snapcode            │
    └────────────────────────────────────────────────────────────────────────────┘
    ```

### 4.1. Компоненты JavaScript

| Модуль | Ответственность |
|---|---|
| `snapcode-language` | Lexer, parser, AST, formatter и source map. |
| `snapcode-semantics` | Области видимости, типы, разрешение имён и проверка аргументов. |
| `snapcode-ir` | Независимая от XML промежуточная модель проекта Snap!. |
| `snapcode-snap12` | Реестр selector-ов и XML-adapter для Snap! 12.2.0. |
| `snapcode-decompiler` | Преобразование XML → IR → SnapCode, readable/canonical/lossless режимы и `raw_*` fallback. |
| `snapcode-editor` | Встроенная панель редактора, автоматическая проверка, диагностика и взаимодействие с IDE Snap!. |
| `snapcode-cli` | Node.js-команды `check`, `compile`, `decompile`, `format`, `catalog` и `test`. |
| `snapcode-conformance` | Golden-тесты, round-trip и проверка selector-ов. |

Все runtime-компоненты выполняются на JavaScript внутри модифицированного Snap! 12.2.0. Конечному пользователю не требуется Java Runtime, сервер или отдельный launcher.

CLI использует те же JavaScript-модули, что и встроенный редактор. В CLI и в редакторе запрещается поддерживать две разные реализации parser-а, semantic analyzer или XML adapter-а.

Отступы преобразуются в логические токены `INDENT` и `DEDENT` до синтаксического анализа. Реализация может использовать собственный lexer или JavaScript-библиотеку, но итоговая грамматика должна соответствовать разделу 7.


### 4.2. Почему компилятор встраивается в Snap!

Панель SnapCode выполняется в том же браузерном JavaScript-окружении, что и модифицированный Snap! 12.2.0. Поэтому компилятор может напрямую использовать общие объекты проекта, штатный serializer и штатный механизм загрузки XML.

Отдельный сервис не требуется.

Цепочка выполнения:

```text
Редактор SnapCode
        ↓
JavaScript lexer/parser
        ↓
AST
        ↓
Snap IR
        ↓
Snap! XML serializer
        ↓
штатная загрузка проекта
```

Преимущества встроенной архитектуры:

- не требуется Java Runtime;
- не требуется локальный HTTP-сервис;
- не требуется localhost-порт и токен;
- не требуется launcher или фоновый процесс;
- проще установка offline-сборки;
- редактор имеет прямой доступ к текущему проекту Snap!;
- логика CLI и редактора может использовать общий JavaScript-код.

Node.js применяется только для разработки, автоматических тестов и запуска CLI вне Snap!.


    ## 5. Исходные файлы

    ### 5.1. Один файл

    Минимальный проект хранится в одном UTF-8 файле:

    ```snapcode
    snapcode 1.0
    target snap "12.2.0"

    project "Demo":
        scene "Scene 1":
            sprite "Cat":
                on green_flag:
                    move(10)
    ```

    ### 5.2. Модульный проект

    ```text
    project/
    ├── project.snapcode
    ├── scenes/
    │   └── main.snapcode
    ├── sprites/
    │   ├── cat.snapcode
    │   └── enemy.snapcode
    └── assets/
        ├── cat.svg
        └── meow.wav
    ```

    Подключение выполняется статически:

    ```snapcode
    import "scenes/main.snapcode"
    import "sprites/cat.snapcode"
    ```

    Правила:

    - Путь вычисляется относительно импортирующего файла.
    - Один и тот же канонический путь загружается один раз.
    - Циклический импорт является ошибкой `SC1203`.
    - Максимальная глубина цепочки импортов — 64. Превышение является ошибкой `SC1204`.
    - Файл может содержать объявления, но ровно один модуль сборки должен объявить `project`.
    - Для работы панели поддерживается виртуальная файловая система: основной документ и вложения передаются сервису одним запросом.

    ## 6. Лексика

    - Кодировка: UTF-8 без требования BOM.
    - Перевод строки: `LF` или `CRLF`; форматтер выводит `LF`.
    - Отступ: ровно 4 пробела на уровень. Табуляция вне строк запрещена.
    - Комментарий: от `#` до конца строки.
    - Идентификатор: Unicode-буква или `_`, далее буквы, цифры и `_`.
    - Имена объектов и selector-ы допускают строковую форму, поэтому любые имена Snap! можно представить без потерь.
    - Строки: `"..."`, `'...'`, многострочные `"""..."""`; escape-последовательности `\\`, `\n`, `\r`, `\t`, `\"`, `\'`, `\uXXXX`, `\UXXXXXXXX`.
    - Числа: целые, десятичные, экспоненциальные; специальный `nan` и бесконечности в обычном коде запрещены, но доступны через `raw_value`.
    - Логические литералы: `true`, `false`.
    - Пустое значение Snap!: `nil`.
    - Зарезервированные слова нельзя использовать как незаключённые в кавычки имена.

    ## 7. Базовая грамматика

    Ниже приведена нормативная сокращённая EBNF. Полная ANTLR-грамматика при реализации должна быть эквивалентна ей.

    ```ebnf
    file          = header, { importDecl | topDecl } ;
    header        = "snapcode", version, NEWLINE,
                    "target", "snap", string, NEWLINE ;
    importDecl    = "import", string, NEWLINE ;
    topDecl       = projectDecl | fragmentDecl | blockDef ;
    projectDecl   = "project", string, ":", suite ;
    sceneDecl     = "scene", string, ":", suite ;
    stageDecl     = "stage", ":", suite ;
    spriteDecl    = "sprite", string, [ "extends", string ], ":", suite ;
    suite         = NEWLINE, INDENT, statement, { statement }, DEDENT ;
    statement     = declaration | assignment | command | event | control
                | blockDef | assetDecl | watcherDecl | rawDecl ;
    expression    = literal | name | list | unary | binary | call | ring
                | primitiveExpr | customExpr | rawValue ;
    event         = "on", eventSpec, ":", suite ;
    command       = call, NEWLINE | primitiveCommand | customCommand ;
    primitiveCommand = "primitive", string, "(", [args], ")",
                    [ ":", primitiveSuites ] ;
    customCommand = "custom", scope, string, "(", [args], ")",
                    [ ":", primitiveSuites ] ;
    primitiveSuites = suite | NEWLINE, INDENT,
                    { "script", integer, ":", suite }, DEDENT ;
    rawDecl       = ("raw_block" | "raw_xml"), rawMeta, tripleString ;
    ```

    Операторы приоритета, от сильного к слабому:

    1. Вызов, индекс и атрибут.
    2. Унарные `not`, `-`, `+`.
    3. `*`, `/`, `mod`.
    4. `+`, `-`.
    5. Сравнения `==`, `!=`, `<`, `<=`, `>`, `>=`, `in`.
    6. `and`.
    7. `or`.
    8. Условное выражение `a if condition else b`.

    ## 8. Модель проекта

## 8. Каталог соответствий SnapCode и selector-ов

Таблица соответствий должна строиться по внутренним selector-ам Snap! 12.2.0. Названия визуальных блоков и локализованные подписи не являются идентификаторами.

Нормативным источником каталога является `SpriteMorph.prototype.primitiveBlocks()` из `objects.js` Snap! 12.2.0. Ручные предположительные названия блоков использовать запрещено.

| SnapCode | Selector Snap! 12.2.0 | Назначение |
|---|---|---|
| `move(n)` | `forward` | Переместить спрайт. |
| `turn(n)` | `turn` | Повернуть спрайт. |
| `turn_left(n)` | `turnLeft` | Повернуть против часовой стрелки. |
| `point_in_direction(n)` | `setHeading` | Задать направление. |
| `goto(x, y)` | `gotoXY` | Перейти в координаты. |
| `change_x(n)` | `changeXPosition` | Изменить X. |
| `set_x(n)` | `setXPosition` | Установить X. |
| `change_y(n)` | `changeYPosition` | Изменить Y. |
| `set_y(n)` | `setYPosition` | Установить Y. |
| `say(text)` | `bubble` | Показать текст. |
| `say(text, seconds)` | `doSayFor` | Показать текст на время. |
| `think(text)` | `doThink` | Показать мысль. |
| `think(text, seconds)` | `doThinkFor` | Показать мысль на время. |
| `play_sound(name)` | `playSound` | Запустить звук. |
| `broadcast(message)` | `doBroadcast` | Отправить сообщение. |
| `broadcast_and_wait(message)` | `doBroadcastAndWait` | Отправить сообщение и ждать. |
| `wait(seconds)` | `doWait` | Подождать. |
| `repeat(n)` | `doRepeat` | Повторить вложенный скрипт. |
| `if(condition)` | `doIf` | Выполнить условие. |
| `if(condition) ... else ...` | `doIfElse` | Выполнить одну из ветвей. |
| `set(variable, value)` | `doSetVar` | Установить переменную. |
| `change(variable, value)` | `doChangeVar` | Изменить переменную. |
| `show()` | `show` | Показать объект. |
| `hide()` | `hide` | Скрыть объект. |

Каталог должен генерироваться автоматически из исходного кода Snap! и сохраняться в машинно-читаемом формате. Если selector отсутствует в каталоге, компилятор обязан выдать ошибку вместо попытки угадать нужный блок.

    ### 8.1. Заголовок

    ```snapcode
    snapcode 1.0
    target snap "12.2.0"
    ```

    Компилятор отклоняет неизвестную major-версию SnapCode. Несовпадение `target` с адаптером считается ошибкой, если не указан явный режим миграции.

    ### 8.2. Проект и сцены

    ```snapcode
    project "Adventure":
        notes "Учебный проект"
        selected_scene "Main"

        scene "Main":
            setting hyper_ops = true
            setting ternary_booleans = false
            setting inheritance = true
            setting pen_color_model = option("hsv")
            global var score: any = 0
    ```

    Snap! сохраняет проекты как XML и позволяет импортировать XML через меню или перетаскиванием файла в окно.[cite:90][cite:93] XML 12.2.0 поддерживает контейнер проекта с несколькими сценами; адаптер SnapCode обязан сохранять порядок сцен и выбранную сцену.[cite:19]

    Поддерживаемые настройки сцены:

    - `unified_palette`, `show_categories`, `show_palette_buttons`;
    - `click_to_run`, `drag_data`, `hide_empty_categories`, `hide_sprites`;
    - `strict_types`, `pen_color_model`;
    - `thread_safe`, `hyper_ops`, `ternary_booleans`, `codify`, `inheritance`, `sublist_ids`;
    - пользовательские категории, скрытые примитивы, code headers и code mappings;
    - роли и шаблоны сцен.

    ### 8.3. Stage

    ```snapcode
    stage:
        size 480, 360
        color color(255, 255, 255, 1.0)
        tempo 60
        volume 100
        pan 0
        costume "Backdrop 1"
        local var level = 1
    ```

    Stage имеет собственные костюмы, звуки, переменные, пользовательские блоки и скрипты. Скрипты Stage используют тот же синтаксис, что и скрипты спрайта, но статическая проверка запрещает команды, доступные только спрайту.

    ### 8.4. Спрайты

    ```snapcode
    sprite "Cat":
        position 0, 0
        heading 90
        scale 1.0
        rotation_style option("all around")
        visible true
        draggable true
        local var health: number = 100
    ```

    Полная декларация спрайта поддерживает:

    - имя, индекс в corral и выбранность;
    - `x`, `y`, направление, масштаб, громкость, панораму, инструмент;
    - стиль вращения, видимость, перетаскивание и скрытие в corral;
    - перо, текущий костюм, костюмы и звуки;
    - локальные переменные, пользовательские блоки и скрипты;
    - anchor/parts, exemplar, наследуемые атрибуты, nesting и solution/template metadata;
    - непрозрачные расширения XML.

    ## 9. Значения и типы

    ### 9.1. Типы SnapCode

    | Тип | Значение |
    |---|---|
    | `any` | Любое значение Snap!. |
    | `number` | Число. |
    | `text` | Строка. |
    | `boolean` | `true` или `false`. |
    | `list<T>` | Snap!-список; обычный или linked. |
    | `color` | RGBA-цвет. |
    | `option` | Значение выпадающего меню Snap!. |
    | `sprite`, `stage`, `object` | Ссылка на объект проекта. |
    | `costume`, `sound` | Медиаобъект. |
    | `command`, `reporter<T>`, `predicate` | Первоклассный скрипт/кольцо. |
    | `continuation` | Продолжение Snap!. |
    | `xml` | Непрозрачное сериализованное значение. |

    ### 9.2. Литералы

    ```snapcode
    42
    3.14
    "text"
    true
    nil
    [1, 2, "three"]
    linked_list(1, 2, 3)
    color(80, 80, 80, 1.0)
    option("space")
    object("Cat")
    ```

    Snap! рассматривает списки как первоклассные значения и поддерживает как императивные операции изменения, так и функциональные операции `map`, `keep`, `combine` и другие.[cite:25] Поэтому список в IR не сводится к XML-массиву: сохраняются его вид, идентичность, ссылки и режим linked/atomic.

    ### 9.3. Переменные

    ```snapcode
    global var score: number = 0
    local var health: number = 100
    script var i: number = 0

    score = 10
    score += 1
    ```

    Области поиска:

    1. Параметр пользовательского блока или кольца.
    2. Скриптовая переменная.
    3. Локальная переменная спрайта/Stage.
    4. Глобальная переменная сцены.

    Явные формы `global.score`, `self.health` и `script.i` снимают неоднозначность. При декомпиляции неоднозначное имя всегда выводится с квалификатором.

    ## 10. Скрипты и события

    ### 10.1. Удобные события

    ```snapcode
    on green_flag:
        move(10)

    on key("space"):
        say("Jump!", 1)

    on message("start"):
        broadcast("ready")

    on clone_start:
        show()
    ```

    Это синтаксический сахар над selector-ами Snap!:

    | SnapCode | Selector |
    |---|---|
    | `on green_flag` | `receiveGo` |
    | `on key(k)` | `receiveKey` |
    | `on message(m)` | `receiveMessage` |
    | `on clone_start` | `receiveOnClone` |
    | `on interaction(kind)` | `receiveInteraction` |
    | `on condition(expr)` | `receiveCondition` |
    | `on user_edit(kind)` | `receiveUserEdit` |

    ### 10.2. Последовательность

    Команды одного suite сериализуются как последовательные дочерние элементы `<block>` внутри `<script>`. Вложенный reporter/predicate сериализуется внутри входа родительского блока. C-слот сериализуется вложенным `<script>`. Именно selector, например `receiveGo` или `doRepeat`, определяет встроенный блок; локализованный текст блока в XML не используется как его идентификатор.[cite:19][cite:101]

    ### 10.3. Управление

    ```snapcode
    repeat 10:
        move(10)

    while touching("edge"):
        turn(15)

    if score > 10:
        say("Win")
    else:
        say("Keep going")

    for item in items:
        say(item)
    ```

    Удобные формы преобразуются в `doRepeat`, `doUntil`/условие с отрицанием, `doIfElse` и `doForEach`. Компилятор не обязан имитировать поведение цикла на Java: он создаёт блоки Snap!, а выполняет их Snap!.

    ## 11. Встроенные блоки

    ### 11.1. Удобные псевдонимы

    ```snapcode
    move(10)                 # forward
    turn(15)                 # turn
    point_in_direction(90)   # setHeading
    goto(0, 0)               # gotoXY
    say("Hello", 2)          # doSayFor
    play_sound("Meow")       # playSound
    broadcast("start")       # doBroadcast
    ```

    Псевдоним — только функция форматтера и компилятора. В Snap IR всегда хранится selector версии 12.2.0.

    ### 11.2. Канонический вызов

    Каждый известный примитив можно записать без псевдонима:

    ```snapcode
    primitive "forward"(10)
    primitive "gotoXY"(0, 0)
    value = primitive "reportProduct"(6, 7)
    condition = primitive "reportEquals"(value, 42)
    ```

    C-блок с одним script-слотом:

    ```snapcode
    primitive "doRepeat"(10):
        script 1:
            primitive "forward"(10)
    ```

    C-блок с несколькими script-слотами:

    ```snapcode
    primitive "doIfElse"(score > 0):
        script 1:
            say("positive")
        script 2:
            say("zero or negative")
    ```

    Нормативные правила:

    - Selector обязан существовать в закреплённом реестре, кроме формы `raw_block`.
    - Тип блока, число входов, допустимые типы и script-слоты берутся из machine-readable каталога Snap! 12.2.0.
    - `primitive` с command selector допустим как statement; reporter/predicate — как expression; hat — только в позиции начала скрипта.
    - Значение `option("...")` отлично от обычной строки, потому что XML использует специальный option-узел.
    - Dev-примитивы требуют `setting allow_dev_primitives = true`.

    ## 12. Пользовательские блоки

    Snap! сохраняет пользовательские блоки вместе с проектом и умеет экспортировать набор глобальных блоков как XML-библиотеку.[cite:91] SnapCode представляет определение отдельно от вызова, чтобы разрешить рекурсию и взаимные ссылки в две фазы.

    ```snapcode
    blockdef global command "draw polygon %n %n" category "motion":
        input sides type number min 3 default 4
        input length type number min 0 default 50
        local temp: number
        body:
            repeat sides:
                move(length)
                turn(360 / sides)

    on green_flag:
        custom global "draw polygon %n %n"(6, 40)
    ```

    Полное объявление входа может задавать:

    - внутреннее имя и placeholder из block spec;
    - Snap slot type (`%s`, `%n`, `%b`, `%l`, `%cmdRing`, `%repRing` и другие);
    - default, options, readonly, irreplaceable;
    - separator, collapse label, expand label;
    - initial count, min и max для variadic input;
    - upvar и multiple-input semantics.

    Поддерживаются типы определений `command`, `reporter`, `predicate` и `hat`, области `global` и `local`, helper/primitive/customized primitive, strict types, translations, code header/mapping, комментарий, локальные переменные определения и дополнительные редакторские скрипты.

    ## 13. Кольца и метапрограммирование

    ```snapcode
    var double = ring reporter(x):
        return x * 2

    var move_twice = ring command(steps):
        move(steps)
        move(steps)

    var positives = keep(ring predicate(x):
        return x > 0
    , values)
    ```

    IR хранит кольцо как context: вид выражения, формальные входы, переменные, receiver/origin и outer context. Snap! позволяет исследовать программу как синтаксическое дерево через `split by blocks` и собирать её обратно через `join`; эти операции должны проходить через канонический слой без упрощения.[cite:92]

    Продолжения представлены специальным значением:

    ```snapcode
    var k: continuation = primitive "reportCallCC"(...)
    ```

    Если декомпилятор не может восстановить контекст или продолжение в удобной форме, используется `raw_value`, а не потеря значения.

    ## 14. Костюмы и звуки

    ```snapcode
    sprite "Cat":
        costume "Idle" from "assets/cat-idle.svg" center (64, 64)
        costume "Run" from "assets/cat-run.png" center (64, 64)
        sound "Meow" from "assets/meow.wav"
        current_costume "Idle"
    ```

    Режимы:

    - `from "path"` — внешний файл модульного проекта;
    - `embedded "data:..."` — data URI для однофайловой декомпиляции;
    - `media_ref "id"` — ссылка на общую media-секцию;
    - `raw_value` — неизвестный формат медиа.

    Импорт Snap! также принимает изображения и звуки через меню Import, поэтому media-слой должен сохранять имя, центр костюма, тип изображения, частоту/данные звука и идентичность ссылок.[cite:90]

    ## 15. Наблюдатели и интерфейс проекта

    ```snapcode
    watch global.score:
        style slider
        position 10, 10
        size 100, 20
        range 0, 100
        visible true
    ```

    Сохраняются watcher target/scope, getter или variable name, style, положение, размер, цвет, slider min/max и видимость. Нераспознанные атрибуты watcher остаются в extension map.

    ## 16. XML Snap! 12.2.0

    ### 16.1. Источник истины

    Адаптер строится по официальному исходному коду `jmoenig/Snap`, тег `v12.2.0`, а именно по сериализатору и загрузчику проекта, реестру `primitiveBlocks()` и model-классам.[cite:19][cite:33] Документация полезна для семантики, но XML-структура определяется кодом версии, потому что пользовательская надпись на блоке и selector — разные сущности.

    ### 16.2. Верхний уровень

    Нормализованная форма проекта:

    ```xml
    <project name="Demo" app="Snap! 12.2.0, https://snap.berkeley.edu" version="2">
    <notes></notes>
    <thumbnail></thumbnail>
    <snapcode version="1.0" encoding="base64">...</snapcode>
    <scenes select="1">
        <scene name="Scene 1">
        ...
        </scene>
    </scenes>
    </project>
    ```

    `snapcode` — расширение fork-а. Обычный Snap! 12.2.0 загружает проект по известным узлам, но при повторном сохранении в немодифицированной версии может отбросить расширение; поэтому исходный `.snapcode` остаётся первичным артефактом. В режиме максимальной совместимости исходник помещается также в sidecar-файл, а XML остаётся стандартным.

    ### 16.3. Сцена

    Порядок логических секций адаптера:

    1. `notes`, palette и `hidden`.
    2. template metadata.
    3. `headers`, `code`.
    4. глобальные `blocks` и customized `primitives`.
    5. `stage`.
    6. глобальные `variables`.

    ### 16.4. Stage и спрайт

    Stage содержит настройки, перьевой bitmap, костюмы, звуки, переменные, блоки, скрипты и список спрайтов. Спрайт содержит свойства положения и отображения, costume/sound collections, локальные blocks/variables/scripts и данные наследования/вложенности.[cite:19]

    ### 16.5. Скрипты и блоки

    ```xml
    <script x="10" y="10">
    <block s="receiveGo"></block>
    <block s="doRepeat">
        <l>10</l>
        <script>
        <block s="forward"><l>10</l></block>
        </script>
    </block>
    </script>
    ```

    - Встроенный блок: `<block s="selector">`.
    - Чтение переменной: `<block var="name">`.
    - Пользовательский блок: `<custom-block s="block spec" ...>`.
    - Последовательность команд: соседние block-узлы в одном script.
    - Reporter/predicate: block-узел внутри позиции входа.
    - C-slot: вложенный `script`.
    - Variadic input: `list` как контейнер входов, не обязательно как runtime list-value.
    - Комментарии блока и скрипта сериализуются отдельно.

    ### 16.6. Значения

    | XML | Snap IR |
    |---|---|
    | `<l>text</l>` | Текстовое/скалярное поле ввода. |
    | `<l><option>space</option></l>` | Значение выпадающего меню. |
    | `<bool>true</bool>` | Логическое значение. |
    | `<list>...</list>` | Snap List или variadic input — смысл определяется контекстом. |
    | `<ref id="N"/>` | Ссылка на ранее зарегистрированный объект. |
    | `<costume ...>` | Костюм. |
    | `<sound ...>` | Звук. |
    | `<context ...>` | Кольцо, скрипт как значение или контекст. |

    Генератор обязан экранировать `&`, `<`, `>`, кавычки в атрибутах и все символы, требуемые XML-процессором. XML собирается через StAX/DOM, а не конкатенацией непроверенных строк.

    ### 16.7. Идентичность и ссылки

    IR присваивает стабильный внутренний UUID каждому ссылочному объекту. XML writer в детерминированном обходе преобразует UUID в последовательные числовые `id`; повторные появления выводятся как `<ref id="...">`. `mediaID` ведётся отдельно. На сравнение проектов нельзя полагаться через буквальное равенство ID: conformance проверяет граф объектов и семантику.

    ## 17. Компиляция

    Порядок фаз обязателен:

    1. Нормализация UTF-8 и переводов строк.
    2. Lexing с `INDENT`/`DEDENT`.
    3. Parsing в CST.
    4. Построение AST с source ranges.
    5. Загрузка импортов и обнаружение циклов.
    6. Предобъявление сцен, объектов, переменных и block definitions.
    7. Разрешение имён и областей видимости.
    8. Проверка типов и ограничений receiver-а.
    9. Lowering удобных конструкций в selector-ориентированный Snap IR.
    10. Проверка IR по реестру Snap! 12.2.0.
    11. Детерминированная раскладка скриптов.
    12. XML serialization.
    13. Повторный безопасный parse созданного XML.
    14. Опциональная загрузка в тестовый экземпляр Snap! и экспорт обратно.

    ### 17.1. Раскладка скриптов

    Если координаты не указаны, применяется детерминированная сетка:

    - начальная позиция `(20, 20)`;
    - вертикальный интервал между независимыми скриптами — 40 logical units плюс оценённая высота предыдущего стека;
    - после достижения высоты 1200 начинается новая колонка;
    - явные `layout x, y` имеют приоритет;
    - декомпилятор сохраняет исходные координаты в metadata, но форматтер может скрывать их в обычном режиме.

    ## 18. Декомпиляция

    ### 18.1. Алгоритм

    1. Безопасно разобрать XML.
    2. Проверить корень, serializer version и target metadata.
    3. Создать таблицы `id`, `mediaID`, спрайтов, variables и block definitions.
    4. Построить Snap IR без изменения порядка.
    5. Разрешить selector-ы по реестру 12.2.0.
    6. Распознать удобные формы (`repeat`, `if`, `move`, операторы и события).
    7. Для известных, но не имеющих псевдонима блоков вывести `primitive`.
    8. Для неизвестных блоков вывести `raw_block`.
    9. Для неизвестных значений или узлов вывести `raw_value`/`raw_xml`.
    10. Отформатировать SnapCode и прикрепить исходные XML-фрагменты к source map.

    ### 18.2. Режимы

    | Режим | Поведение |
    |---|---|
    | `readable` | Максимум удобных конструкций; layout и служебные ID скрыты. |
    | `canonical` | Selector-ориентированный код, детерминированный и удобный для тестов. |
    | `lossless` | Сохраняет layout, неизвестные атрибуты, порядок и raw-фрагменты. |

    ### 18.3. Неизвестный блок

    ```snapcode
    raw_block command selector "futureSelector" xml """
    <block s="futureSelector"><l>value</l></block>
    """
    ```

    `raw_block` содержит:

    - ожидаемую форму: `command`, `reporter`, `predicate`, `hat` или `unknown`;
    - selector, если он обнаружен;
    - исходный XML ровно одного блока;
    - список ссылок на внешние ID, если фрагмент не самодостаточен;
    - checksum исходного текста.

    Компилятор вставляет фрагмент обратно только после проверки well-formedness, запрета DTD/external entities и отсутствия конфликтующих ID. Все ограничения безопасности из раздела 22.1 должны применяться рекурсивно ко вложенным фрагментам `raw_xml`; частичная проверка или проверка только верхнего уровня недостаточна. Это реализует выбранный режим: произвольный проект Snap! декомпилируется без молчаливого удаления незнакомых конструкций.

    ### 18.4. Семантический round-trip

    Гарантия формулируется так:

    ```text
    Snap XML → IR → SnapCode → IR → Snap XML'
    ```

    `XML'` обязан быть семантически эквивалентен исходному проекту для распознанной модели, но не обязан совпадать побайтно: порядок атрибутов, служебные ID, пробелы, thumbnail и нормализация media data могут отличаться. В `lossless` режиме неизвестные фрагменты должны сохраняться побайтно после нормализации переводов строк, если их ссылки не требуют перенумерации.

    ## 19. Панель редактора

    ### 19.1. Внешний вид

    Интерфейс повторяет не чат, а механику выдвижной панели ассистента:

    - На правой границе окна Snap! находится круглая кнопка `</>` с tooltip `SnapCode`.
    - Нажатие открывает панель справа; повторное нажатие закрывает её.
    - Панель занимает 36% ширины окна по умолчанию, минимум 360 px и максимум 70%; левая граница перетаскивается.
    - Верхняя строка содержит имя файла, состояние сохранения и кнопки `Build & Load`, `Check`, `Format`, `Decompile`, `Export` и `⋮`.
    - Основная область — только редактор кода, без истории сообщений, аватаров и поля чата.
    - Нижняя область — вкладки `Problems`, `Output`, `XML Preview` и `Outline`.
    - `Esc` закрывает панель, не удаляя буфер. `Ctrl/Cmd+Enter` выполняет `Build & Load`.

    Для редактора рекомендуется CodeMirror 6: это расширяемый web-компонент редактора с программным API.[cite:75] Monaco функциональнее и поддерживает IntelliSense/валидацию, но тяжелее; он остаётся допустимой заменой.[cite:76][cite:79]

    ### 19.2. Поведение кнопок

    | Действие | Результат |
    |---|---|
    | `Build & Load` | Компиляция; при отсутствии ошибок вызов штатной загрузки проекта Snap!. |
    | `Check` | Lex/parse/semantic validation без генерации и загрузки. |
    | `Format` | Форматирование с сохранением курсора через source mapping. |
    | `Decompile` | Экспорт текущего проекта в XML-модель и преобразование в SnapCode. |
    | `Export` | Сохранение `.snapcode`, XML или папки проекта. |
    | `XML Preview` | Read-only нормализованный XML и diff с последней сборкой. |

    Исходный код Snap! предоставляет загрузку строки проекта через собственный serializer/IDE path; интеграция должна вызывать этот штатный путь, а не вручную заменять DOM или внутренние объекты.[cite:19] Перед загрузкой выполняется backup текущего проекта. После успешной загрузки панель остаётся открытой и восстанавливает выделение.

    ### 19.3. Синхронизация

    Состояния документа:

    - `clean` — буфер совпадает с последней успешной сборкой;
    - `dirty` — текст изменён;
    - `checking` — идёт проверка;
    - `error` — последняя сборка не удалась;
    - `loaded` — скомпилированный XML принят Snap!;
    - `external-change` — блоки Snap! изменены после последней сборки.

    Если пользователь меняет блоки визуально, панель показывает banner: `Проект изменён вне SnapCode`. Доступны действия `Decompile changes`, `Keep code` и `Compare`. Автоматически перезаписывать несохранённый код запрещено.

    ### 19.4. Открытие проекта

    - Если XML содержит embedded SnapCode с совпадающим checksum, панель открывает этот исходник.
    - Если embedded source отсутствует, запускается декомпиляция `readable`.
    - Если XML создан другой версией Snap!, панель предлагает миграцию в адаптер 12.2.0, но не выполняет её молча.
    - Если сервис Java недоступен, панель остаётся редактором read-only/буфером и показывает кнопку `Start or reconnect Java service`.

    ## Актуализированная архитектура SnapCode

    Проект реализуется как модификация оригинального Snap! 12.2.0 offline, а не как отдельное приложение и не как внешняя сервисная система.

    Принятые ограничения:
    - Не использовать Java runtime у конечного пользователя.
    - Не использовать локальный HTTP-сервис, localhost API, фоновый процесс, protocol handler или launcher.
    - Не требовать от пользователя отдельного запуска дополнительных компонентов после установки.
    - Изменять существующие файлы Snap! 12.2.0 и встраивать SnapCode непосредственно в исходную offline-сборку.

    Итоговая архитектура:
    - Компилятор и декомпилятор реализуются полностью на JavaScript.
    - Выполнение компиляции и декомпиляции происходит внутри вкладки браузера, в том же окружении, где работает Snap!.
    - Установщик вносит изменения в оригинальный Snap! 12.2.0, добавляя код SnapCode в существующие файлы проекта.
    - После установки пользователь запускает уже модифицированный Snap! обычным способом.

    Цепочка компиляции:
    .snapcode -> lexer -> parser -> AST -> Snap IR -> XML -> стандартная загрузка проекта Snap!

    Цепочка декомпиляции:
    текущий XML проекта Snap! -> Snap IR -> AST -> .snapcode

    ## Установка

    Целевые платформы:
    - Windows
    - Linux

    Поддерживаемые архитектуры:
    - x86-64
    - ARM64

    Сценарий установки:
    1. Пользователь помещает папку мода в папку с Snap! 12.2.0 offline.
    2. На Windows запускает install.exe.
    3. На Linux запускает install.sh.
    4. Установщик создаёт резервные копии изменяемых файлов, внедряет SnapCode в исходную сборку и создаёт деинсталлятор.
    5. После установки пользователь открывает уже изменённый Snap! как обычный offline Snap!.

    Принцип интеграции:
    - модифицируется оригинальный snap.html;
    - SnapCode загружается всегда;
    - отдельный launcher не используется;
    - отдельный режим без SnapCode не предусматривается.

    ## Интерфейс редактора

    - В правом верхнем углу Snap! располагается кнопка «Редактор».
    - По нажатию открывается правая панель шириной около 40%.
    - Панель поддерживает ручное изменение ширины.
    - Проверка кода выполняется автоматически.
    - Замена блокового проекта результатом компиляции выполняется только после подтверждения пользователя.

    ## Открытие проектов

    Если открывается обычный XML-проект Snap! без встроенного SnapCode:
    - Snap! открывает проект как обычно.
    - Мод предлагает декомпилировать проект.
    - Если пользователь отказывается, в центре окна редактора отображается кнопка «Декомпилировать проект».

    ## Хранение исходника

    - Основной исходник проекта может существовать как `.snapcode`.
    - Встроенная копия исходника SnapCode сохраняется внутри XML проекта.
    - Отдельный `.snapcode` не создаётся автоматически рядом с XML.
    - При необходимости пользователь экспортирует `.snapcode` вручную.
    - При каждой новой сборке XML полностью пересобирается из текущего исходника.

    ## Конфликты между кодом и блоками

    Если после последней синхронизации были изменены и код, и блоки:
    - система не выбирает автоматически источник истины;
    - пользователю показывается диалог выбора;
    - возможны действия: использовать код, использовать блоки, сравнить, отменить.

    ## Assets

    - Пользователь открывает `.snapcode` и связанную папку `assets`.
    - Ресурсы читаются по пользовательскому выбору, обрабатываются в памяти и встраиваются в XML проекта.
    - При невозможности обработать ресурс сборка завершается ошибкой.
    - Вопрос поддержки GIF оставлен открытым и требует отдельного решения.




### 19.4. Открытие проекта (дополнение)

Если XML содержит встроенный SnapCode с подходящими `version`, `target` и checksum, редактор предлагает открыть этот исходник.

Если встроенный SnapCode отсутствует, редактор выполняет декомпиляцию текущего XML-проекта:

```text
XML → Snap IR → AST → SnapCode
```

Если XML создан другой версией Snap!, редактор не выполняет молчаливую миграцию. Он показывает предупреждение и предлагает выбрать действие:

```text
The project was created for another Snap! version.
Choose an action:
- Open Read-only
- Migrate to Snap! 12.2.0
- Cancel
```

Если текущий SnapCode содержит несохранённые изменения, исходник не заменяется автоматически. Пользователь выбирает:

```text
Keep Code
Use Decompiled Project
Compare
Cancel
```

Отдельный Java-сервис или сообщение о его недоступности отсутствуют, потому что компилятор и декомпилятор выполняются внутри Snap! на JavaScript.

---
## 20. Внутренний JavaScript API

SnapCode не использует локальный HTTP API и не запускает отдельный сервис. Компоненты взаимодействуют через внутренние JavaScript-модули модифицированного Snap!.

### 20.1. Интерфейс компилятора

```javascript
const result = await snapcode.compile({
    source,
    filename,
    target: 'snap-12.2.0',
    options
});
```

Результат:

```javascript
{
    ok: true,
    xml,
    ir,
    diagnostics,
    sourceMap
}
```

### 20.2. Интерфейс проверки

```javascript
const result = snapcode.check({
    source,
    filename,
    target: 'snap-12.2.0'
});
```

Проверка не создаёт XML и не изменяет текущий проект.

### 20.3. Интерфейс декомпиляции

```javascript
const result = await snapcode.decompile({
    xml,
    filename,
    mode: 'readable'
});
```

Поддерживаемые режимы:

- `readable`;
- `canonical`;
- `lossless`.

### 20.4. Интерфейс форматтера

```javascript
const result = snapcode.format({
    source,
    filename
});
```

### 20.5. Взаимодействие с Snap! IDE

После успешной сборки редактор вызывает штатный путь загрузки проекта Snap!, используя XML serializer и модель IDE. Редактор не должен вручную заменять отдельные DOM-узлы проекта.

Node.js CLI использует те же API-модули вне браузера. Различается только способ передачи файлов и отображения результата.

---

    ## 21. Диагностика

    | Диапазон | Категория |
    |---|---|
    | `SC1xxx` | Файлы, кодировка, импорт, версия языка. |
    | `SC2xxx` | Лексика и синтаксис. |
    | `SC3xxx` | Имена, области и типы. |
    | `SC4xxx` | Каталог блоков и receiver constraints. |
    | `SC5xxx` | XML, ссылки, media и raw fragments. |
    | `SC6xxx` | Round-trip и несовместимость версии. |
    | `SC7xxx` | Локальный сервис и интеграция UI. |

    Каждая ошибка содержит стабильный код, severity, файл, диапазон, понятное сообщение и по возможности исправление. Парсер накапливает независимые ошибки, но ограничивает их число, чтобы одно повреждение отступа не породило сотни сообщений.

## 22. Безопасность

### 22.1. Безопасность XML

XML разбирается безопасным parser-ом. Запрещаются:

- `DOCTYPE`;
- external entities;
- external DTD;
- XInclude;
- внешние schema/style resources;
- неожиданные корневые элементы;
- конфликтующие или висячие ID;
- чрезмерная глубина вложенности;
- чрезмерное количество XML-узлов.

`raw_xml` принимается только после проверки well-formedness и структурных ограничений. Он не может заменить корневой `<project>` и не может создавать внешние сущности.

### 22.2. Безопасность исходного кода

SnapCode не исполняется как JavaScript. Запрещается использовать `eval`, `Function` и другие механизмы исполнения исходного текста.

`primitive` только создаёт описание блока Snap! и не запускает произвольный JavaScript.

> **Важно:** selector `reportURL` (`url %s`) позволяет загружать содержимое произвольного URL во время выполнения. Хотя это штатная функция Snap!, SnapCode компилятор должен выдавать предупреждение `SC4402` при использовании этого selector-а, если не задана настройка `setting allow_network = true`. Это аналогично ограничениям dev-примитивов.

### 22.3. Безопасность файлов

Импорт ресурсов запрещает:

- выход за корень проекта через `..`;
- symbolic-link escape;
- чтение произвольных системных файлов;
- автоматическую загрузку URL без allowlist;
- неограниченное чтение файлов.

### 22.4. Лимиты

Лимиты на размеры файлов, глубину AST/XML, количество узлов и размеры ресурсов не устанавливаются. Компилятор обрабатывает файлы произвольного размера без искусственных ограничений.

### 22.5. Dev-примитивы

Dev-примитивы отключены по умолчанию и требуют:

```snapcode
setting allow_dev_primitives = true
```

Оборудование Arduino не требуется для обычного тестирования.

### 22.6. Отсутствие сетевого сервиса

SnapCode runtime не слушает сетевые порты и не создаёт localhost API. Это исключает необходимость в токенах, CORS-политике и защите локального HTTP-сервиса.

---

    ## 23. Тестирование

    ### 23.1. Уровни

    - Lexer/parser unit tests: корректные и ошибочные отступы, строки, Unicode, recovery.
    - Semantic tests: scope, типы, receiver, пользовательские блоки, рекурсия.
    - Selector conformance: минимум один compile/decompile test на каждую из 256 записей реестра.
    - XML golden tests: эталонные фрагменты, экспортированные Snap! 12.2.0.
    - Project tests: сцены, спрайты, inheritance, media, watchers, lists, contexts.
    - Round-trip: XML → code → XML и code → XML → code.
    - UI tests: панель, resize, горячие клавиши, diagnostics, внешние изменения.
    - Security tests: XXE, billion laughs, path traversal, oversized nesting, ID collision.

    ### 23.2. Критерии приёмки

    1. Каждый обычный и dev selector из приложения A либо типизированно компилируется, либо отклоняется только из-за выключенного dev-режима.
    2. Проекты с неизвестным selector декомпилируются с `raw_block`, не теряя XML этого блока.
    3. Проект, созданный компилятором, импортируется Snap! 12.2.0 штатным механизмом XML.[cite:90]
    4. Все ссылки `id`/`ref` и `mediaID` разрешаются; висячие ссылки являются ошибкой.
    5. Повторная компиляция одного и того же входа даёт детерминированный XML, кроме явно помеченных volatile-полей.
    6. При ошибке сборки текущий проект Snap! не заменяется.
    7. Визуальные изменения обнаруживаются и никогда не перезаписывают dirty-буфер без подтверждения.
    8. Форматтер идемпотентен: повторное форматирование не меняет результат.

    ## 24. Этапы реализации

    Полный охват остаётся конечным требованием, но реализация выполняется вертикальными слоями:

    1. **Основа:** IR, реестр 12.2.0, XML reader/writer, CLI и round-trip минимального проекта.
    2. **Язык:** lexer/parser, imports, variables, expressions, scripts и diagnostics.
    3. **Примитивы:** автоматическая генерация каталога и canonical `primitive` для всех selector-ов.
    4. **Высокий уровень:** псевдонимы, события, control sugar и форматтер.
    5. **Объектная модель:** сцены, Stage, спрайты, inheritance, nesting, watchers.
    6. **Процедуры:** custom blocks, rings, contexts, metaprogramming и continuations.
    7. **Медиа:** costume/sound, media IDs, embedded и extracted assets.
    8. **Декомпилятор:** readable/canonical/lossless и `raw_*` fallback.
   9. Интеграция: JavaScript-модуль редактора, кнопка </>, правая панель шириной 36%, Build & Load, автоматическая проверка через 3 секунды, красные подчёркивания ошибок и external-change flow.
    10. **Укрепление:** полная conformance matrix, fuzzing XML/parser и security limits.

    Этап не считается законченным без compile, decompile и round-trip тестов соответствующей функции.

    ## 25. Ответы на исходные вопросы

    1. **Как устроен XML?** Иерархия `project → scenes → scene → stage → sprites`, с отдельными collections переменных, блоков, scripts и media; ссылки образуют граф поверх дерева.
    2. **Какие узлы соответствуют блокам?** Встроенные — `<block s="selector">`, переменные — `<block var="name">`, пользовательские — `<custom-block s="spec">`.
    3. **Как хранятся вложенность и циклы?** Вложенный reporter является дочерним block-входом, тело C-блока — дочерним `<script>`.
    4. **Как хранятся события?** Hat-блок является первым блоком самостоятельного script, например `receiveGo`.
    5. **Как хранятся переменные?** Значения находятся в `variables/variable`, а чтение/изменение использует имя и область receiver-а.
    6. **Как кодируются строки?** UTF-8 плюс обязательное XML escaping; option и boolean не смешиваются с обычным текстом.
    7. **Как поддерживаются спрайты?** Каждый sprite имеет свойства, assets, variables, blocks и scripts; порядок и selected index сохраняются.
    8. **Как добавляются звуки и костюмы?** Через media values/data URI либо отдельные assets, с сохранением `mediaID` и ссылок.
    9. **Как обрабатываются пользовательские блоки?** Двухфазно: сначала все definitions, затем bodies и calls; учитываются global/local scope и typed inputs.
    10. **Как проверяется XML?** Safe parse, структурная валидация IR, ссылки, каталог selector-ов и пробная загрузка в Snap! 12.2.0.
    11. **Поддерживаются ли несколько файлов?** Да, через статический `import` и VFS панели.
    12. Как обеспечивается совместимость? Целевая версия — только Snap! 12.2.0. Реестр selector-ов генерируется из `SpriteMorph.prototype.primitiveBlocks()` в `objects.js`, а XML-структура определяется serializer-ом из `store.js`. Компилятор и декомпилятор работают на JavaScript внутри модифицированного Snap!. Node.js CLI использует те же модули для разработки и тестирования. Отдельный Java adapter, Java Runtime и локальный HTTP-сервис не требуются.

    ## 26. Нормативные запреты

- ИИ и пользователь не должны генерировать Snap XML вручную для обычных операций.
- Компилятор не должен угадывать selector по переведённому тексту блока.
- Selector должен существовать в каталоге Snap! 12.2.0 либо быть явно представлен через разрешённый `raw_block`.
- Декомпилятор не должен молча удалять неизвестный узел, атрибут, media-объект или ссылку.
- Удобный псевдоним не должен менять семантику канонического selector-а.
- JavaScript не должен исполнять исходный SnapCode через `eval`, `Function` или эквивалентные механизмы.
- `raw_xml` не должен содержать `DOCTYPE`, external entities, external DTD или внешний ресурс.
- Компилятор не должен читать файлы за пределами корня проекта.
- URL-ресурсы не должны загружаться без явного allowlist-разрешения.
- Dev-примитивы не должны использоваться без `allow_dev_primitives = true`.
- Проект Snap! не должен заменяться, пока `check` или `compile` завершился ошибкой.
- Автоматическая проверка не должна изменять текущий проект.
- `Build & Load` должен запрашивать подтверждение перед заменой текущего проекта.
- При одновременных изменениях кода и блоков система не должна выбирать источник автоматически.
- Нельзя считать побайтное совпадение XML единственным критерием round-trip.
- Нельзя считать встроенный `<snapcode>` единственным источником исходника, потому что стандартный Snap! может удалить неизвестное расширение.
- Node.js CLI является инструментом разработки и не должен быть обязательным runtime-компонентом для конечного пользователя.
- Java Runtime, локальный Java-сервис и localhost API не являются обязательными компонентами SnapCode.


# Раздел 27. Зафиксированные архитектурные решения

Этот раздел имеет нормативный приоритет над более ранними описаниями проекта. Если старый раздел противоречит настоящему разделу, используется настоящая редакция.

## 27.1. Целевая версия

SnapCode разрабатывается только для **Snap! 12.2.0**.

Все selector-ы, типы входов, структура XML, правила сериализации и поведение декомпилятора относятся к версии Snap! 12.2.0.

Поддержка других версий Snap! не входит в первую реализацию. Для будущих версий должны создаваться отдельные адаптеры:

```text
snapcode-snap12
snapcode-snap13
...
```

SnapCode не должен определять версию Snap! по догадке. Версия должна быть указана в исходном файле:

```snapcode
snapcode 1.0
target snap "12.2.0"
```

## 27.2. Исполнение внутри Snap!

Компилятор, декомпилятор, форматтер и диагностический анализатор выполняются на JavaScript внутри модифицированной offline-сборки Snap! 12.2.0.

Итоговая схема:

```text
SnapCode editor
        ↓
JavaScript lexer
        ↓
JavaScript parser
        ↓
AST
        ↓
Snap IR
        ↓
Snap! XML serializer
        ↓
штатная загрузка проекта Snap!
```

Обратная схема:

```text
текущий проект Snap!
        ↓
штатная XML-сериализация
        ↓
Snap IR
        ↓
AST
        ↓
SnapCode formatter
```

Конечному пользователю не требуется:

- Java Runtime;
- отдельный Java-сервис;
- локальный HTTP-сервер;
- localhost API;
- фоновый процесс;
- отдельный launcher;
- Node.js для запуска редактора.

## 27.3. CLI

CLI является отдельным инструментом разработчика и тестирования. Он не требуется конечному пользователю и не является частью runtime Snap!.

CLI может быть реализован на Node.js и использовать те же JavaScript-модули, что и встроенный редактор.

Минимальные команды:

```text
snapcode check <file.snapcode>
snapcode compile <file.snapcode> --out <file.xml>
snapcode decompile <file.xml> --out <file.snapcode>
snapcode format <file.snapcode>
snapcode catalog
snapcode test
```

CLI и встроенный редактор обязаны использовать общие реализации:

```text
lexer
parser
semantic analyzer
formatter
Snap IR
selector catalog
XML adapter
diagnostics
```

Нельзя поддерживать отдельную логику компиляции для CLI и для встроенного редактора. Различаться могут только интерфейсы запуска и отображения результатов.

## 27.4. Отменённые архитектурные варианты

Следующие решения считаются устаревшими и не должны использоваться в новой реализации:

- Java 21 как язык основного компилятора;
- ANTLR 4 для runtime-компилятора;
- локальный Java HTTP-сервис;
- localhost API;
- отдельный launcher;
- запуск JAR рядом с Snap!;
- обязательный Java Runtime у пользователя.

Старые описания этих вариантов сохраняются только как исторический материал и не являются нормативной частью проекта.

## 27.5. Источник истины

Нормативными источниками проекта являются:

1. исходный код Snap! 12.2.0;
2. `objects.js` для каталога примитивов;
3. `byob.js` для пользовательских блоков и их структуры;
4. `store.js` для XML-сериализации и загрузки;
5. SnapCode AST и Snap IR;
6. тесты совместимости.

Старые таблицы, созданные вручную по названиям визуальных блоков, не имеют нормативной силы.

***

# Раздел 28. Встроенный редактор SnapCode

## 28.1. Назначение

В модифицированный Snap! 12.2.0 встраивается редактор SnapCode.

Редактор предназначен для:

- написания SnapCode;
- автоматической проверки;
- подсветки ошибок;
- форматирования;
- компиляции в XML;
- загрузки результата в текущий проект Snap!;
- декомпиляции обычных XML-проектов Snap! в SnapCode.

Редактор не является чат-интерфейсом и не должен имитировать окно диалога с ассистентом.

## 28.2. Кнопка редактора

В интерфейсе Snap! размещается кнопка с надписью:

```text
</>
```

Tooltip кнопки:

```text
SnapCode
```

Кнопка открывает и закрывает правую панель редактора.

Название пользовательской кнопки не должно быть `Editor`. Слово `Editor` может использоваться в tooltip, заголовке панели или меню, но основная кнопка отображает символ `</>`.

## 28.3. Правая панель

Правая панель:

- открывается у правой границы окна Snap!;
- занимает **36% ширины окна** по умолчанию;
- имеет минимальную ширину 360 px;
- имеет максимальную ширину 70% окна;
- может изменять ширину перетаскиванием левой границы;
- не закрывает полностью область сцены, если это технически возможно;
- сохраняет выбранную ширину между открытиями текущей сессии.

Верхняя строка панели содержит:

- имя текущего SnapCode-файла;
- состояние документа;
- кнопку `Build & Load`;
- кнопку `Check`;
- кнопку `Format`;
- кнопку `Decompile`;
- кнопку `Export`;
- кнопку закрытия панели.

## 28.4. Язык интерфейса

Интерфейс SnapCode в первой версии создаётся на английском языке.

Основные элементы интерфейса:

```text
SnapCode
Build & Load
Check
Format
Decompile
Export
Problems
Output
XML Preview
Outline
Unsaved changes
Project changed outside SnapCode
Keep Code
Use Blocks
Compare
Cancel
```

Тексты диагностических сообщений также должны быть на английском языке.

## 28.5. Проверка с задержкой

Проверка выполняется автоматически через **3 секунды после последнего введённого символа**.

Алгоритм:

1. Пользователь изменяет текст.
2. Предыдущий таймер проверки отменяется.
3. Запускается новый таймер на 3000 миллисекунд.
4. Если пользователь снова изменяет текст, таймер снова отменяется.
5. После 3 секунд без изменений запускаются lexer, parser и semantic checker.
6. Результат отображается в редакторе и на панели `Problems`.

Автоматическая проверка не должна автоматически:

- создавать XML;
- изменять текущий проект Snap!;
- запускать проект;
- удалять пользовательские блоки;
- перезаписывать сохранённый файл.

## 28.6. Подчёркивание ошибок

При наличии ошибки редактор обязан подчёркивать ошибочный участок красной волнистой линией.

Диагностика должна содержать:

```text
code
severity
message
file
start line
start column
end line
end column
suggestions
```

Пример:

```json
{
    "code": "SC2304",
    "severity": "error",
    "message": "Unknown primitive selector: forwad",
    "file": "project.snapcode",
    "start": {
        "line": 8,
        "column": 9
    },
    "end": {
        "line": 8,
        "column": 15
    },
    "suggestions": [
        "forward"
    ]
}
```

Для ошибки:

```snapcode
primitive "forwad"(10)
```

красным подчёркивается только:

```text
forwad
```

а не вся строка.

Если ошибка относится ко всей конструкции, например к незакрытому блоку, подчёркивается максимально маленький доступный диапазон:

```snapcode
repeat 10:
    move(10)
```

Если отсутствует тело цикла, подчёркивается заголовок `repeat 10:`.

## 28.7. Состояния документа

Редактор использует следующие состояния:

```text
clean
dirty
checking
error
ready
loaded
external-change
```

Описание:

- `clean` — код совпадает с последней успешной сборкой;
- `dirty` — код изменён после последней сборки;
- `checking` — выполняется автоматическая проверка;
- `error` — последняя проверка или сборка завершилась ошибкой;
- `ready` — ошибок нет, но проект ещё не загружен;
- `loaded` — результат успешно загружен в Snap!;
- `external-change` — блоки Snap! изменились после последней синхронизации.

## 28.8. Build & Load

Кнопка `Build & Load` выполняет операции в следующем порядке:

1. остановить предыдущую сборку этого документа;
2. выполнить lexer;
3. выполнить parser;
4. выполнить semantic analysis;
5. построить Snap IR;
6. проверить Snap IR по каталогу Snap! 12.2.0;
7. сериализовать IR в XML;
8. безопасно разобрать созданный XML повторно;
9. при успехе показать предварительный результат;
10. запросить подтверждение перед заменой текущего проекта;
11. после подтверждения загрузить XML через штатный механизм Snap!.

Если на любой стадии появляется ошибка:

- текущий проект Snap! не изменяется;
- старый XML не заменяется;
- редактор показывает диагностические сообщения;
- результат сборки помечается как `error`.

## 28.9. Декомпиляция

Если пользователь открывает обычный XML-проект Snap! без встроенного SnapCode:

1. Snap! открывает проект штатным способом.
2. SnapCode анализирует текущую модель проекта.
3. Проект преобразуется в Snap IR.
4. Snap IR преобразуется в AST.
5. AST форматируется в SnapCode.
6. В редакторе появляется предложение открыть результат декомпиляции.

Декомпиляция не должна автоматически удалять текущий код пользователя.

Если в редакторе есть несохранённые изменения, показывается диалог:

```text
The current SnapCode document has unsaved changes.
Choose an action:
- Keep Code
- Use Decompiled Blocks
- Compare
- Cancel
```

***

# Раздел 29. Нормативный синтаксис SnapCode

## 29.1. Основной синтаксис

Основным синтаксисом считается синтаксис второй части спецификации:

```snapcode
snapcode 1.0
target snap "12.2.0"

project "Demo":
    scene "Main":
        sprite "Cat":
            on green_flag:
                move(10)
```

Имена проекта, сцены и спрайта в нормативном синтаксисе записываются как строки.

## 29.2. Устаревшие формы

Следующие формы считаются устаревшими:

```snapcode
sprite Cat:
when_green_flag:
set("score", 0)
when_key("space"):
```

Они могут поддерживаться декомпилятором в режиме совместимости, но formatter обязан преобразовывать их в нормативную форму:

```snapcode
sprite "Cat":
    on green_flag:
        set(score, 0)

    on key("space"):
        say("Jump!", 1)
```

Новые программы, создаваемые пользователем или ИИ, должны использовать только нормативную форму.

## 29.3. Полный заголовок файла

Полный файл SnapCode обязан начинаться с:

```snapcode
snapcode 1.0
target snap "12.2.0"
```

Эти строки определяют:

- версию языка;
- целевую версию Snap!;
- адаптер XML;
- режим проверки совместимости.

Файл без заголовка может быть принят только в коротком режиме редактора или CLI при явно указанном значении:

```text
--target snap-12.2.0
```

В таком случае компилятор должен добавить заголовок во внутреннюю модель, но не обязан автоматически изменять исходный файл.

## 29.4. Минимальный короткий фрагмент

Для вставки небольшого фрагмента в редактор разрешается использовать код без заголовка:

```snapcode
on green_flag:
    move(10)
```

Такой фрагмент не является самостоятельным проектом. Он компилируется только в контексте выбранного спрайта или текущего объекта Snap!.

Если контекст не выбран, компилятор выдаёт ошибку:

```text
SC3001: A project, scene or receiver context is required for this fragment.
```

## 29.5. Проект, сцена и спрайт

Полный проект имеет следующую структуру:

```snapcode
project "Demo":
    scene "Main":
        stage:
            ...

        sprite "Cat":
            ...

        sprite "Enemy":
            ...
```

`project` может содержать одну или несколько сцен.

Каждая сцена имеет один Stage и ноль или больше спрайтов.

В MVP разрешается только одна сцена, но синтаксис должен оставаться совместимым с несколькими сценами.

## 29.6. Одна сцена по умолчанию

Для коротких проектов можно использовать сокращённую форму:

```snapcode
snapcode 1.0
target snap "12.2.0"

project "Demo":
    sprite "Cat":
        on green_flag:
            move(10)
```

Если `scene` отсутствует, компилятор создаёт сцену:

```text
Main
```

Правило действует только при отсутствии явных нескольких сцен.

Если в одном файле объявлена хотя бы одна явная сцена, все спрайты должны находиться внутри сцены.

## 29.7. Несколько сцен

Поддержка нескольких сцен входит в модель языка и декомпилятора.

В первой реализации допускается ограничить компиляцию одной сценой, но при встрече второй сцены компилятор должен выдать понятную ошибку, а не молча удалить её:

```text
SC4102: Multiple scenes are not supported by the current MVP compiler.
```

Декомпилятор не должен удалять дополнительные сцены. Если MVP не умеет вывести их в удобной форме, он обязан использовать каноническую форму или `raw_xml`.

***

# Раздел 30. Типы данных и переменные

## 30.1. Поддерживаемые типы MVP

В первой версии SnapCode поддерживаются следующие типы:

```text
int
str
any
```

> **Примечание:** В полной спецификации (раздел 9.1) используется тип `number`. В MVP `int` является кратким псевдонимом `number`. Компилятор должен принимать оба варианта — `int` и `number` — как эквивалентные. В каноническом выводе форматтер использует `number`.

### `int`

Целое число:

```snapcode
42
-10
0
```

### `str`

Строка:

```snapcode
"Hello"
"Прыжок!"
```

### `any`

Любое значение Snap!, включая:

- число;
- строку;
- список;
- логическое значение;
- цвет;
- объект;
- костюм;
- звук;
- контекст;
- значение неизвестного типа.

## 30.2. Логические значения

Логические значения разрешаются как встроенные значения:

```snapcode
true
false
```

В MVP они не являются отдельным обязательным пользовательским типом. Внутренне они могут храниться как `any`.

## 30.3. Переменные

Объявление переменной:

```snapcode
global var score: int = 0
local var name: str = "Cat"
script var i: int = 0
```

Если тип не указан:

```snapcode
global var value = 0
```

тип выводится из начального значения как `int`.

Если значение не позволяет вывести тип:

```snapcode
global var value = primitive "reportAttributeOf"(...)
```

переменная получает тип `any`.

## 30.4. Области видимости

Поддерживаются следующие области:

1. параметр пользовательского блока или кольца;
2. переменная скрипта;
3. локальная переменная спрайта или Stage;
4. глобальная переменная сцены.

При разрешении имени используется такой порядок:

```text
parameter
script
local receiver
global scene
```

Ближайшая область скрывает внешнюю область с тем же именем.

## 30.5. Явные квалификаторы

Для устранения неоднозначности используются квалификаторы:

```snapcode
global.score
self.health
script.i
```

`self` означает текущий Stage или спрайт.

Примеры:

```snapcode
score = 10
self.health -= 1
global.score += 1
script.i += 1
```

Если имя неоднозначно, компилятор обязан выдать ошибку или потребовать квалификатор. Он не должен выбирать область случайно.

## 30.6. Переменная другого спрайта

Для чтения значения переменной другого объекта используется форма:

```snapcode
object("Dog").health
```

или сокращённая форма:

```snapcode
Dog.health
```

Форма `Dog.health` разрешается только если `Dog` однозначно является объектом проекта.

Эта форма компилируется в получение свойства другого объекта через соответствующий Snap! reporter.

Пример:

```snapcode
if Dog.health < 1:
    say("Dog is defeated")
```

## 30.7. Запись в переменную другого спрайта

Запись в переменную другого спрайта запрещена в MVP:

```snapcode
Dog.health = 0
```

вызывает ошибку:

```text
SC3404: Writing to variables of another receiver is not supported.
```

Изменение состояния другого спрайта выполняется через:

- сообщение;
- пользовательский блок;
- кольцо;
- собственный обработчик события.

Пример:

```snapcode
Dog.receive("reset")
```

или:

```snapcode
broadcast("reset_dog")
```

## 30.8. Присваивание

Основная форма:

```snapcode
score = 10
score += 1
score -= 1
```

Для совместимости допускается форма:

```snapcode
set(score, 10)
change(score, 1)
```

Форма с именем в строке:

```snapcode
set("score", 10)
change("score", 1)
```

считается устаревшей и может использоваться только в compatibility mode.

## 30.9. Проверка типов

При отключённом строгом режиме компилятор допускает присваивание значений типа `any`.

Выполнение арифметической операции над строкой может быть принято компилятором только если хотя бы один аргумент имеет тип `any`. Если оба аргумента имеют тип `str`, выдаётся ошибка:

```text
SC3307: Arithmetic operation requires an integer or any value.
```

При включённом `strict_types`:

- `int` нельзя присвоить `str`;
- `str` нельзя присвоить `int`;
- результат reporter должен соответствовать объявленному типу;
- несовместимость типов является ошибкой, а не предупреждением.

***

# Раздел 31. Циклы и lowering

## 31.1. Общий принцип

Удобные конструкции SnapCode не исполняются JavaScript-компилятором. Компилятор преобразует их в Snap IR и соответствующие блоки Snap!.

```text
SnapCode control syntax
        ↓
lowering
        ↓
Snap selector
        ↓
XML block
```

## 31.2. `repeat`

Исходный код:

```snapcode
repeat 10:
    move(10)
```

Преобразуется в:

```text
selector: doRepeat
input 1: 10
slot 1:
    forward(10)
```

XML-модель:

```xml
<block s="doRepeat">
    <l>10</l>
    <script>
        <block s="forward">
            <l>10</l>
        </block>
    </script>
</block>
```

## 31.3. `while`

Форма:

```snapcode
while condition:
    body
```

поддерживается как синтаксический сахар.

Если целевая версия Snap! не содержит отдельного `while`, компилятор преобразует конструкцию в `doUntil` с отрицанием:

```text
while condition:
    body
```

становится:

```text
repeat until:
    not(condition)
```

Внутренняя модель:

```text
doUntil(
    reportNot(condition),
    body
)
```

Если `condition` невозможно представить как predicate Snap!, компилятор выдаёт:

```text
SC4205: The while condition cannot be lowered to a Snap! predicate.
```

## 31.4. `for item in list`

Форма:

```snapcode
for item in items:
    say(item)
```

преобразуется в selector `doForEach`.

Внутренняя модель:

```text
doForEach(
    upvar = item,
    list = items,
    body = [
        say(item)
    ]
)
```

Переменная цикла:

- создаётся как локальная переменная цикла;
- доступна только внутри тела цикла;
- не обязана существовать после завершения цикла;
- может быть переиспользована во вложенном цикле с отдельной областью.

Пример:

```snapcode
for item in items:
    if item > 0:
        say(item)
```

## 31.5. `for i in range`

Форма:

```snapcode
for i in range(1, 10):
    say(i)
```

разрешается только если в каталоге Snap! 12.2.0 существует соответствующая семантика диапазонного цикла.

Компилятор проверяет наличие подходящего selector-а и входов в каталоге. Если selector или нужная структура отсутствуют, код отклоняется:

```text
SC4210: Range iteration is not available in the selected Snap! target.
```

При наличии подходящей формы lowering выполняется в диапазонный цикл Snap!:

```text
doFor(
    upvar = i,
    start = 1,
    end = 10,
    body = [...]
)
```

Нельзя автоматически заменять `range` на JavaScript-цикл. Это должно оставаться блоком, выполняемым Snap!.

## 31.6. Арифметические цепочки

Выражение:

```snapcode
a + b + c
```

разбирается как:

```text
(a + b) + c
```

Если selector поддерживает вариативный вход, компилятор может представить выражение как один variadic-блок.

Если selector не поддерживает нужный формат, используется вложенная форма:

```text
reportVariadicSum(
    reportVariadicSum(a, b),
    c
)
```

Форматтер canonical обязан использовать детерминированную форму.

## 31.7. `in`

Оператор:

```snapcode
item in items
```

понимается как проверка наличия элемента в списке.

Он lowering-ится в соответствующий list predicate Snap!, например:

```text
reportListContainsItem(items, item)
```

Оператор `in` не должен автоматически применяться к строкам, объектам или произвольным значениям, если каталог Snap! 12.2.0 не предоставляет соответствующую операцию.

***

# Раздел 32. Каталог selector-ов

## 32.1. Источник каталога

Каталог selector-ов должен генерироваться из:

```javascript
SpriteMorph.prototype.primitiveBlocks()
```

в файле `objects.js` целевой версии Snap! 12.2.0.

В предоставленном исходном файле обнаружено 256 записей:

```text
command: 114
reporter: 104
predicate: 26
hat: 9
ring: 3
dev: 30
ordinary: 226
```

Число 256 относится к записям каталога, включая dev-примитивы.

## 32.2. Формат каталога

Каталог должен храниться в машинно-читаемом формате, например JSON:

```json
{
    "target": "snap-12.2.0",
    "serializerVersion": 2,
    "source": "SpriteMorph.prototype.primitiveBlocks",
    "selectors": {
        "forward": {
            "type": "command",
            "category": "motion",
            "dev": false,
            "spec": "move %n steps",
            "reports": null,
            "defaults": [10]
        },
        "doRepeat": {
            "type": "command",
            "category": "control",
            "dev": false,
            "spec": "repeat %n %loop",
            "reports": null
        }
    }
}
```

## 32.3. Генерация

Генератор каталога должен:

1. загрузить `objects.js`;
2. найти `SpriteMorph.prototype.primitiveBlocks`;
3. получить объект записей;
4. извлечь selector;
5. извлечь `type`;
6. извлечь `category`;
7. извлечь `dev`;
8. извлечь `spec`;
9. извлечь `reports`;
10. извлечь `defaults`;
11. сохранить версию Snap!;
12. посчитать checksum исходного каталога.

Каталог не должен редактироваться вручную без автоматической проверки.

## 32.4. Проверки каталога

Генератор обязан проверять:

- отсутствие дублирующихся selector-ов;
- наличие типа;
- наличие категории;
- корректность `spec`;
- соответствие количества входов `defaults`;
- наличие selector-а в `SpriteMorph.prototype.blocks`;
- уникальность имени;
- корректность dev-флага.

## 32.5. Нормативная таблица удобных команд

Старая таблица соответствий из раздела 8 первой части считается устаревшей. Нормативная таблица должна строиться на selector-ах.

Минимальные соответствия:

| SnapCode | Selector |
|---|---|
| `move(n)` | `forward` |
| `turn(n)` | `turn` |
| `turn_left(n)` | `turnLeft` |
| `point_in_direction(n)` | `setHeading` |
| `goto(x, y)` | `gotoXY` |
| `change_x(n)` | `changeXPosition` |
| `set_x(n)` | `setXPosition` |
| `change_y(n)` | `changeYPosition` |
| `set_y(n)` | `setYPosition` |
| `say(text)` | `bubble` |
| `say(text, seconds)` | `doSayFor` |
| `think(text)` | `doThink` |
| `think(text, seconds)` | `doThinkFor` |
| `play_sound(name)` | `playSound` |
| `broadcast(message)` | `doBroadcast` |
| `broadcast_and_wait(message)` | `doBroadcastAndWait` |
| `wait(seconds)` | `doWait` |
| `repeat(n)` | `doRepeat` |
| `if(condition)` | `doIf` |
| `if(condition) ... else ...` | `doIfElse` |
| `set(variable, value)` | `doSetVar` |
| `change(variable, value)` | `doChangeVar` |
| `show()` | `show` |
| `hide()` | `hide` |

Если selector отсутствует в машинно-читаемом каталоге, команда не должна компилироваться.

***

# Раздел 33. XML Snap! 12.2.0

## 33.1. Версия сериализатора

В исходном `store.js`:

```javascript
XML_Serializer.prototype.version = 2;
```

Поэтому XML-проект Snap! 12.2.0 должен использовать:

```xml
version="2"
```

Это версия сериализатора Snap!, а не версия SnapCode.

Версия SnapCode указывается отдельно:

```snapcode
snapcode 1.0
target snap "12.2.0"
```

## 33.2. Верхний уровень XML

Фактическая верхнеуровневая структура:

```xml
<project
    name="Demo"
    app="Snap!, https://snap.berkeley.edu"
    version="2">
    <notes></notes>
    <thumbnail></thumbnail>
    <scenes select="1">
        <scene name="Main">
            ...
        </scene>
    </scenes>
</project>
```

Новая версия не должна использовать в качестве стандартной структуры:

```xml
<scenes>
    <scene>
        <stage>
            <sprites>
```

без учёта реального порядка и атрибутов serializer-а.

## 33.3. Сцена

`Scene.prototype.toXML` сериализует сцену с секциями:

```xml
<scene name="Main">
    <notes></notes>
    <palette></palette>
    <hidden></hidden>
    <headers></headers>
    <code></code>
    <blocks></blocks>
    <primitives></primitives>
    <stage>...</stage>
    <variables></variables>
</scene>
```

Наличие конкретных секций зависит от состояния проекта и serializer-а.

Порядок секций должен соответствовать `store.js`.

## 33.4. Stage

Упрощённая структура Stage:

```xml
<stage
    name="Stage"
    width="480"
    height="360"
    costume="0"
    color="255,255,255,1"
    tempo="60"
    threadsafe="false"
    penlog="false"
    volume="100"
    pan="0"
    lines="round"
    ternary="false"
    hyperops="false"
    codify="false"
    inheritance="true"
    sublistIDs="false">
    <pentrails></pentrails>
    <costumes></costumes>
    <sounds></sounds>
    <variables></variables>
    <blocks></blocks>
    <scripts></scripts>
    <sprites select="1"></sprites>
</stage>
```

Значения `width`, `height`, цвета, темп, громкость и другие настройки должны сериализоваться из IR, а не подставляться произвольно.

## 33.5. Спрайт

Структура спрайта:

```xml
<sprite
    name="Cat"
    idx="1"
    x="0"
    y="0"
    heading="90"
    scale="1"
    volume="100"
    pan="0"
    rotation="1"
    draggable="true"
    costume="0"
    color="80,80,80,1"
    pen="tip">
    <costumes></costumes>
    <sounds></sounds>
    <blocks></blocks>
    <variables></variables>
    <scripts></scripts>
</sprite>
```

Точные необязательные атрибуты зависят от состояния спрайта, наследования и наличия медиа.

## 33.6. Скрипты

Независимый скрипт:

```xml
<script x="20" y="20">
    <block s="receiveGo"></block>
    <block s="forward">
        <l>10</l>
    </block>
</script>
```

`x` и `y` являются координатами скрипта на рабочей области.

Последовательность команд хранится как последовательность соседних `<block>` внутри одного `<script>`.

## 33.7. Вложенные C-блоки

Пример `repeat`:

```xml
<block s="doRepeat">
    <l>10</l>
    <script>
        <block s="forward">
            <l>10</l>
        </block>
    </script>
</block>
```

Вложенный reporter хранится как блок внутри входа родительского блока:

```xml
<block s="forward">
    <block s="reportRandom">
        <l>1</l>
        <l>10</l>
    </block>
</block>
```

## 33.8. Значения

Основные формы значений:

```xml
<l>text</l>
```

```xml
<l>
    <option>space</option>
</l>
```

```xml
<l>
    <bool>true</bool>
</l>
```

```xml
<list>
    <item>...</item>
    <item>...</item>
</list>
```

```xml
<block var="score"></block>
```

```xml
<ref id="1"></ref>
```

Генератор обязан использовать XML serializer или безопасный DOM/XML API. Сборка XML обычной конкатенацией строк запрещена.

## 33.9. Исходник SnapCode

Узел `<snapcode>` не является обязательной частью стандартного XML Snap! 12.2.0.

Он может использоваться только как расширение модифицированной версии Snap!, например:

```xml
<snapcode version="1.0" target="12.2.0" checksum="...">
    ...
</snapcode>
```

Обычный Snap! может проигнорировать или удалить неизвестный узел при повторном сохранении. Поэтому встроенный SnapCode не считается единственным способом сохранения исходника.

Нормативным источником является открытый документ `.snapcode`, а XML хранит только дополнительную встроенную копию, если она включена пользователем.

***

# Раздел 34. Синхронизация кода и блоков

## 34.1. Основной источник

В проекте существуют два представления:

```text
SnapCode source
Snap! block project
```

Ни одно из них не должно автоматически перезаписывать другое при конфликте.

## 34.2. Сборка кода

При `Build & Load`:

1. исходный SnapCode проверяется;
2. создаётся новый XML;
3. текущий проект сохраняется во временную резервную копию;
4. пользователю показывается подтверждение;
5. только после подтверждения проект заменяется результатом сборки.

Если сборка завершилась ошибкой, текущий проект остаётся без изменений.

## 34.3. Изменение блоков

Если пользователь изменил блоки в Snap! после последней загрузки SnapCode, состояние становится:

```text
external-change
```

Редактор показывает:

```text
Project changed outside SnapCode.
```

Доступные действия:

```text
Decompile Changes
Keep Code
Compare
Cancel
```

## 34.4. Одновременные изменения

Если изменены и код, и блоки:

- система не выбирает источник автоматически;
- dirty SnapCode не перезаписывается;
- визуальный проект не перезаписывается;
- пользователь должен выбрать действие явно.

## 34.5. Checksum

Checksum встроенного SnapCode вычисляется от нормализованного текста:

1. перевод строк приводится к `LF`;
2. UTF-8 используется как кодировка;
3. пробелы внутри строк сохраняются;
4. завершающие пробелы строк удаляются форматтером;
5. используется SHA-256;
6. результат записывается в hex-формате.

Пример:

```xml
<snapcode
    version="1.0"
    target="12.2.0"
    checksum="sha256:...">
```

Checksum не используется для проверки XML. Он используется только для определения того, соответствует ли встроенный SnapCode текущему исходному тексту.

***

# Раздел 35. Assets и GIF

## 35.1. Поддерживаемые ресурсы MVP

В первой версии поддерживаются:

- PNG;
- JPEG;
- SVG;
- WAV;
- MP3, если его принимает браузер и Snap! 12.2.0.

GIF также поддерживается как импортируемый ресурс.

## 35.2. Ограничения размера

Максимальный размер одного ресурса:

```text
32 MiB
```

Максимальный суммарный размер ресурсов одной сборки:

```text
128 MiB
```

Ограничение применяется до декодирования data URI.

Если лимит превышен, выдаётся ошибка:

```text
SC5207: Asset exceeds the maximum allowed size.
```

## 35.3. GIF

GIF может быть:

- статическим;
- анимированным.

В MVP GIF импортируется как ресурс, если браузер и Snap! могут его отобразить. Если конкретная версия Snap! не сохраняет анимацию GIF в виде, совместимом с текущей моделью Costume, компилятор должен выдать предупреждение:

```text
SC5209: Animated GIF may be imported as a static image by Snap!.
```

Автоматическое преобразование GIF в набор кадров не входит в первую реализацию.

## 35.4. Пути

Путь к ресурсу вычисляется относительно корня проекта:

```snapcode
costume "Cat" from "assets/cat.gif"
sound "Meow" from "assets/meow.wav"
```

Запрещены:

```text
../outside-project.png
```

символические ссылки, ведущие за пределы корня проекта, и URL-ресурсы без отдельного разрешения пользователя.

***

# Раздел 36. Dev-примитивы и тестовое покрытие

## 36.1. Dev-примитивы

Dev-примитивы не используются в обычном SnapCode-коде без явного разрешения:

```snapcode
setting allow_dev_primitives = true
```

Если настройка отсутствует, обращение к dev-selector-у вызывает ошибку:

```text
SC4301: Development primitive is disabled.
```

## 36.2. Оборудование

Следующие примитивы исключаются из обязательного runtime-тестирования MVP:

```text
digitalWrite
pwmWrite
servoWrite
reportConnected
reportDigitalReading
```

Они могут присутствовать в каталоге selector-ов и поддерживаться как канонические `primitive`, но не требуют физического оборудования для обычного набора тестов.

## 36.3. Тестирование dev-примитивов

Для dev-примитивов без оборудования выполняются только:

- проверка наличия в каталоге;
- проверка типа;
- проверка числа входов;
- проверка сериализации;
- проверка десериализации;
- проверка флага `dev`;
- проверка отказа при выключенном dev-режиме.

Физическая проверка Arduino-блоков не входит в критерии приёмки SnapCode MVP.

## 36.4. Обязательное покрытие

Для обычных selector-ов требуется:

```text
catalog test
compile test
decompile test
round-trip test
```

Для dev-selector-ов без оборудования требуется:

```text
catalog test
validation test
serialization test
disabled-mode rejection test
```

***

# Раздел 37. Обновлённый MVP

## 37.1. Возможности MVP

MVP обязан поддерживать:

- SnapCode 1.0;
- target Snap! 12.2.0;
- JavaScript runtime внутри Snap!;
- Node.js CLI для разработки;
- один проект;
- одну сцену;
- Stage;
- несколько спрайтов;
- события `green_flag`, `key`, `message`, `clone_start`;
- переменные `int`, `str`, `any`;
- `set`;
- `change`;
- `move`;
- `turn`;
- `goto`;
- `say`;
- `broadcast`;
- `wait`;
- `repeat`;
- `if`;
- `else`;
- `while`;
- `for item in list`;
- `for i in range(...)` только при наличии соответствующего selector-а;
- автоматическую проверку через 3 секунды;
- красное подчёркивание ошибок;
- генерацию XML;
- загрузку результата в Snap!;
- базовую декомпиляцию XML в SnapCode;
- лимиты ресурсов;
- отказ от dev-примитивов по умолчанию.

## 37.2. Минимальный пример

```snapcode
snapcode 1.0
target snap "12.2.0"

project "Demo":
    scene "Main":
        global var score: int = 0

        sprite "Cat":
            on green_flag:
                score = 0
                goto(0, 0)

                repeat 10:
                    move(10)
                    score += 1

            on key("space"):
                say("Jump!", 1)
                change_y(30)
```

## 37.3. Критерий готовности

MVP считается готовым, если:

1. CLI выполняет `check`.
2. CLI выполняет `compile`.
3. CLI выполняет `decompile`.
4. Встроенный редактор выполняет автоматическую проверку.
5. Ошибки подчёркиваются красным.
6. SnapCode компилируется в XML Snap! 12.2.0.
7. XML загружается штатным механизмом Snap!.
8. Проект запускается в Snap!.
9. Ошибочная сборка не меняет текущий проект.
10. Изменение блоков обнаруживается редактором.
11. Обычный проект Snap! может быть декомпилирован.
12. Физическое оборудование не требуется для прохождения тестов.
13. Один и тот же исходник даёт детерминированный XML.
14. Ресурсы ограничиваются установленными лимитами.

***

## Что ещё нужно исправить в старых разделах

Эти места теперь нужно пометить как устаревшие или заменить:

- раздел 4.1 — старые Java-компоненты;
- раздел 4.2 — локальный HTTP-сервис;
- раздел 8 Части 1 — старая таблица selector-ов;
- раздел 15 Части 1 — старый prompt для ИИ;
- раздел 18 Части 1 — Python или Java;
- раздел 19.4 — недоступный Java-сервис;
- раздел 20 — локальный API;
- раздел 22 — безопасность Java-сервиса;
- раздел 24, этап 9 — Java service;
- раздел 25, пункт 12 — Java adapter/service;
- раздел 26 — запрет, сформулированный только для Java-сервиса.

Ключевое уточнение: по вопросу 6 я выбрал вариант, который считаю наиболее практичным — **полная модель поддерживает `project → scene → stage/sprite`, но для коротких файлов разрешается одна сцена по умолчанию**. MVP использует одну сцену, а структура языка сразу остаётся совместимой с несколькими сценами.




    ## Приложение A. Примитивы 12.2.0

    Каталог ниже сгенерирован из `SpriteMorph.prototype.primitiveBlocks()` официального исходного кода Snap! 12.2.0; selector является нормативным идентификатором XML.[cite:19] Строка `dev` означает, что примитив скрыт в обычном режиме и требует явного разрешения.

    ### Движение (`motion`)

    | Selector XML | Тип | Возвращает | Режим | Текст блока |
    |---|---|---|---|---|
    | `forward` | `command` | `—` | обычный | move %n steps |
    | `turn` | `command` | `—` | обычный | turn $clockwise %n degrees |
    | `turnLeft` | `command` | `—` | обычный | turn $counterclockwise %n degrees |
    | `setHeading` | `command` | `—` | обычный | point in direction %dir |
    | `doFaceTowards` | `command` | `—` | обычный | point towards %dst |
    | `gotoXY` | `command` | `—` | обычный | go to x: %n y: %n |
    | `doGotoObject` | `command` | `—` | обычный | go to %dst |
    | `doGlide` | `command` | `—` | обычный | glide %n secs to x: %n y: %n |
    | `changeXPosition` | `command` | `—` | обычный | change x by %n |
    | `setXPosition` | `command` | `—` | обычный | set x to %n |
    | `changeYPosition` | `command` | `—` | обычный | change y by %n |
    | `setYPosition` | `command` | `—` | обычный | set y to %n |
    | `bounceOffEdge` | `command` | `—` | обычный | if on edge, bounce |
    | `getPosition` | `reporter` | `list` | обычный | position |
    | `xPosition` | `reporter` | `number` | обычный | x position |
    | `yPosition` | `reporter` | `number` | обычный | y position |
    | `direction` | `reporter` | `number` | обычный | direction |

    ### Внешность (`looks`)

    | Selector XML | Тип | Возвращает | Режим | Текст блока |
    |---|---|---|---|---|
    | `doSwitchToCostume` | `command` | `—` | обычный | switch to costume %cst |
    | `doWearNextCostume` | `command` | `—` | обычный | next costume |
    | `getCostumeIdx` | `reporter` | `number` | обычный | costume # |
    | `reportGetImageAttribute` | `reporter` | `number` | обычный | %img of costume %cst |
    | `reportNewCostume` | `reporter` | `costume` | обычный | new costume %l width %dim height %dim |
    | `reportNewCostumeStretched` | `reporter` | `costume` | обычный | stretch %cst x: %n y: %n % |
    | `reportNewCostumeSkewed` | `reporter` | `costume` | обычный | skew %cst to %dir degrees %n % |
    | `doSayFor` | `command` | `—` | обычный | say %s for %n secs |
    | `bubble` | `command` | `—` | обычный | say %s |
    | `doThinkFor` | `command` | `—` | обычный | think %s for %n secs |
    | `doThink` | `command` | `—` | обычный | think %s |
    | `changeEffect` | `command` | `—` | обычный | change %eff effect by %n |
    | `setEffect` | `command` | `—` | обычный | set %eff effect to %n |
    | `getEffect` | `reporter` | `number` | обычный | %eff effect |
    | `clearEffects` | `command` | `—` | обычный | clear graphic effects |
    | `changeScale` | `command` | `—` | обычный | change size by %n |
    | `setScale` | `command` | `—` | обычный | set size to %n % |
    | `getScale` | `reporter` | `number` | обычный | size |
    | `show` | `command` | `—` | обычный | show |
    | `hide` | `command` | `—` | обычный | hide |
    | `reportShown` | `predicate` | `—` | обычный | shown? |
    | `goToLayer` | `command` | `—` | обычный | go to %layer layer |
    | `goBack` | `command` | `—` | обычный | go back %n layers |
    | `doScreenshot` | `command` | `—` | dev | save %imgsource as costume named %s |
    | `reportCostumes` | `reporter` | `list` | dev | wardrobe |
    | `alert` | `command` | `—` | dev | alert %mult%s |
    | `log` | `command` | `—` | dev | console log %mult%s |

    ### Звук (`sound`)

    | Selector XML | Тип | Возвращает | Режим | Текст блока |
    |---|---|---|---|---|
    | `playSound` | `command` | `—` | обычный | play sound %snd |
    | `doPlaySoundUntilDone` | `command` | `—` | обычный | play sound %snd until done |
    | `doPlaySoundAtRate` | `command` | `—` | обычный | play sound %snd at %rate Hz |
    | `doStopAllSounds` | `command` | `—` | обычный | stop all sounds |
    | `reportGetSoundAttribute` | `reporter` | `number` | обычный | %aa of sound %snd |
    | `reportNewSoundFromSamples` | `reporter` | `sound` | обычный | new sound %l rate %rate Hz |
    | `doRest` | `command` | `—` | обычный | rest for %n beats |
    | `doPlayNote` | `command` | `—` | обычный | play note %note for %n beats |
    | `doPlayFrequency` | `command` | `—` | dev | play %n Hz for %n secs |
    | `doSetInstrument` | `command` | `—` | обычный | set instrument to %inst |
    | `doChangeTempo` | `command` | `—` | обычный | change tempo by %n |
    | `doSetTempo` | `command` | `—` | обычный | set tempo to %n bpm |
    | `getTempo` | `reporter` | `number` | обычный | tempo |
    | `changeVolume` | `command` | `—` | обычный | change volume by %n |
    | `setVolume` | `command` | `—` | обычный | set volume to %n % |
    | `getVolume` | `reporter` | `number` | обычный | volume |
    | `changePan` | `command` | `—` | обычный | change balance by %n |
    | `setPan` | `command` | `—` | обычный | set balance to %n |
    | `getPan` | `reporter` | `number` | обычный | balance |
    | `playFreq` | `command` | `—` | обычный | play frequency %n Hz |
    | `stopFreq` | `command` | `—` | обычный | stop frequency |
    | `reportSounds` | `reporter` | `list` | dev | jukebox |

    ### Перо (`pen`)

    | Selector XML | Тип | Возвращает | Режим | Текст блока |
    |---|---|---|---|---|
    | `clear` | `command` | `—` | обычный | clear |
    | `down` | `command` | `—` | обычный | pen down |
    | `up` | `command` | `—` | обычный | pen up |
    | `getPenDown` | `predicate` | `—` | обычный | pen down? |
    | `setColor` | `command` | `—` | обычный | set pen color to %clr |
    | `setPenColorDimension` | `command` | `—` | обычный | set pen %clrdim to %n |
    | `changePenColorDimension` | `command` | `—` | обычный | change pen %clrdim by %n |
    | `getPenAttribute` | `reporter` | `number` | обычный | pen %pen |
    | `setBackgroundColor` | `command` | `—` | обычный | set background color to %clr |
    | `setBackgroundColorDimension` | `command` | `—` | обычный | set background %clrdim to %n |
    | `changeBackgroundColorDimension` | `command` | `—` | обычный | change background %clrdim by %n |
    | `changeSize` | `command` | `—` | обычный | change pen size by %n |
    | `setSize` | `command` | `—` | обычный | set pen size to %n |
    | `doStamp` | `command` | `—` | обычный | stamp |
    | `floodFill` | `command` | `—` | обычный | fill |
    | `write` | `command` | `—` | обычный | write %txt size %n |
    | `reportPenTrailsAsCostume` | `reporter` | `costume` | обычный | pen trails |
    | `reportPentrailsAsSVG` | `reporter` | `costume` | обычный | pen vectors |
    | `doPasteOn` | `command` | `—` | обычный | paste on %spr |
    | `doCutFrom` | `command` | `—` | обычный | cut from %spr |
    | `doDrawOn` | `command` | `—` | обычный | %msk on %spr |
    | `reportColor` | `reporter` | `color` | обычный | color %clr |
    | `reportColorAttribute` | `reporter` | `number` | обычный | %color of color %clr |
    | `reportNewColor` | `reporter` | `color` | обычный | new color %hsbt |

    ### Управление (`control`)

    | Selector XML | Тип | Возвращает | Режим | Текст блока |
    |---|---|---|---|---|
    | `reportHyperZip` | `reporter` | `list` | dev | zip %repRing inputs: %br %s leaf-rank %n %br %s leaf-rank %n |
    | `receiveGo` | `hat` | `—` | обычный | when $greenflag clicked |
    | `receiveKey` | `hat` | `—` | обычный | when %keyHat key pressed %keyName |
    | `receiveInteraction` | `hat` | `—` | обычный | when I am %interaction |
    | `receiveMessage` | `hat` | `—` | обычный | when I receive %msgHat %message |
    | `receiveCondition` | `hat` | `—` | обычный | when %b |
    | `receiveConditionEvent` | `hat` | `—` | обычный | when %b |
    | `getLastMessage` | `reporter` | `text` | dev | message |
    | `doBroadcast` | `command` | `—` | обычный | broadcast %msg %receive |
    | `doBroadcastAndWait` | `command` | `—` | обычный | broadcast %msg %receive and wait |
    | `reportPoll` | `reporter` | `any` | обычный | request %msg %survey |
    | `doWait` | `command` | `—` | обычный | wait %n secs |
    | `doWaitUntil` | `command` | `—` | обычный | wait until %boolUE |
    | `doForever` | `command` | `—` | обычный | forever %loop |
    | `doRepeat` | `command` | `—` | обычный | repeat %n %loop |
    | `doUntil` | `command` | `—` | обычный | repeat until %boolUE %loop |
    | `doFor` | `command` | `—` | обычный | for %upvar = %n to %n %cla |
    | `doIf` | `command` | `—` | обычный | if %b %c %elseif |
    | `doIfElse` | `command` | `—` | обычный | if %b %c else %c |
    | `reportIfElse` | `reporter` | `any` | обычный | if %b then %anyUE else %anyUE |
    | `doStopThis` | `command` | `—` | обычный | stop %stopChoices |
    | `doRun` | `command` | `—` | обычный | run %cmdRing %inputs |
    | `fork` | `command` | `—` | обычный | launch %cmdRing %inputs |
    | `evaluate` | `reporter` | `any` | обычный | call %repRing %inputs |
    | `doReport` | `command` | `—` | обычный | report %s |
    | `doCallCC` | `command` | `—` | dev | run %cmdRing w/continuation |
    | `reportCallCC` | `reporter` | `—` | dev | call %cmdRing w/continuation |
    | `doTellTo` | `command` | `—` | обычный | tell %spr to %cl |
    | `reportAskFor` | `reporter` | `any` | обычный | ask %spr for %repRing %inputs |
    | `receiveOnClone` | `hat` | `—` | обычный | when I start as a clone |
    | `createClone` | `command` | `—` | обычный | create a clone of %cln |
    | `newClone` | `reporter` | `sprite` | обычный | a new clone of %clntrtl |
    | `removeClone` | `command` | `—` | обычный | delete this clone |
    | `receiveUserEdit` | `hat` | `—` | обычный | when %edit is edited %message |
    | `doDefineBlock` | `command` | `—` | обычный | define %upvar %s %repRing |
    | `doSetBlockAttribute` | `command` | `—` | обычный | set %byob of block %repRing to %s |
    | `doDeleteBlock` | `command` | `—` | обычный | delete block %repRing |
    | `reportBlockAttribute` | `reporter` | `any` | обычный | %block of block %repRing |
    | `reportEnvironment` | `reporter` | `any` | обычный | this %env |
    | `receiveSlotEvent` | `hat` | `—` | обычный | when slot %inputSlot signals %slotEvent |
    | `doSetSlot` | `command` | `—` | обычный | set slot %inputSlot to %s |
    | `doPauseAll` | `command` | `—` | обычный | pause all $pause |
    | `doSwitchToScene` | `command` | `—` | обычный | switch to scene %scn %send |
    | `reportPipe` | `reporter` | `any` | обычный | pipe %s $arrowRight %mult%repRing |
    | `reportNewProcess` | `reporter` | `process` | обычный | new process %cmdRing %inputs |
    | `reportProcessAttribute` | `reporter` | `any` | обычный | %procAttribs of process %p |
    | `reportProcessState` | `predicate` | `—` | обычный | is process %p %procStates ? |
    | `doChangeProcess` | `command` | `—` | обычный | %procActions process %p |

    ### Сенсоры (`sensing`)

    | Selector XML | Тип | Возвращает | Режим | Текст блока |
    |---|---|---|---|---|
    | `reportTouchingObject` | `predicate` | `—` | обычный | touching %col ? |
    | `reportTouchingColor` | `predicate` | `—` | обычный | touching %clr ? |
    | `reportColorIsTouchingColor` | `predicate` | `—` | обычный | color %clr is touching %clr ? |
    | `reportAspect` | `reporter` | `—` | обычный | %asp at %loc |
    | `reportStackSize` | `reporter` | `number` | dev | stack size |
    | `reportFrameCount` | `reporter` | `number` | dev | frames |
    | `reportYieldCount` | `reporter` | `number` | dev | yields |
    | `reportThreadCount` | `reporter` | `number` | dev | processes |
    | `doAsk` | `command` | `any` | обычный | ask %s and wait |
    | `reportLastAnswer` | `reporter` | `any` | dev | answer |
    | `getLastAnswer` | `reporter` | `any` | обычный | answer |
    | `reportMousePosition` | `reporter` | `list` | обычный | mouse position |
    | `reportMouseX` | `reporter` | `number` | обычный | mouse x |
    | `reportMouseY` | `reporter` | `number` | обычный | mouse y |
    | `reportMouseDown` | `predicate` | `—` | обычный | mouse down? |
    | `reportKeyPressed` | `predicate` | `—` | обычный | key %key pressed? |
    | `reportRelationTo` | `reporter` | `number` | обычный | %rel to %dst |
    | `doResetTimer` | `command` | `—` | обычный | reset timer |
    | `reportTimer` | `reporter` | `—` | dev | timer |
    | `getTimer` | `reporter` | `number` | обычный | timer |
    | `reportAttributeOf` | `reporter` | `any` | обычный | %att of %spr |
    | `reportObject` | `reporter` | `agent` | обычный | object %self |
    | `reportURL` | `reporter` | `text` | обычный | url %txt |
    | `doSetGlobalFlag` | `command` | `—` | обычный | set %setting to %b |
    | `reportGlobalFlag` | `predicate` | `—` | обычный | is %setting on? |
    | `reportDate` | `reporter` | `number` | обычный | current %dates |
    | `reportGet` | `reporter` | `any` | обычный | my %get |
    | `reportAudio` | `reporter` | `number` | обычный | microphone %audio |
    | `doSetVideoTransparency` | `command` | `—` | обычный | set video transparency to %n |
    | `reportVideo` | `reporter` | `number` | обычный | video %vid on %self |

    ### Операторы (`operators`)

    | Selector XML | Тип | Возвращает | Режим | Текст блока |
    |---|---|---|---|---|
    | `reportVariadicSum` | `reporter` | `number` | обычный | %sum |
    | `reportDifference` | `reporter` | `number` | обычный | %n \\u2212 %n |
    | `reportVariadicProduct` | `reporter` | `number` | обычный | %product |
    | `reportQuotient` | `reporter` | `number` | обычный | %n / %n |
    | `reportRound` | `reporter` | `number` | обычный | round %n |
    | `reportMonadic` | `reporter` | `number` | обычный | %fun of %n |
    | `reportPower` | `reporter` | `number` | обычный | %n ^ %n |
    | `reportModulus` | `reporter` | `number` | обычный | %n mod %n |
    | `reportAtan2` | `reporter` | `number` | обычный | atan2 %n ÷ %n |
    | `reportVariadicMin` | `reporter` | `any` | обычный | %min |
    | `reportVariadicMax` | `reporter` | `any` | обычный | %max |
    | `reportRandom` | `reporter` | `number` | обычный | pick random %ns to %ns |
    | `reportVariadicEquals` | `predicate` | `—` | обычный | %all= |
    | `reportVariadicNotEquals` | `predicate` | `—` | обычный | %all!= |
    | `reportVariadicLessThan` | `predicate` | `—` | обычный | %all< |
    | `reportVariadicLessThanOrEquals` | `predicate` | `—` | обычный | %all<= |
    | `reportVariadicGreaterThan` | `predicate` | `—` | обычный | %all> |
    | `reportVariadicGreaterThanOrEquals` | `predicate` | `—` | обычный | %all>= |
    | `reportVariadicAnd` | `predicate` | `—` | обычный | %all |
    | `reportVariadicOr` | `predicate` | `—` | обычный | %any |
    | `reportNot` | `predicate` | `—` | обычный | not %b |
    | `reportBoolean` | `predicate` | `—` | обычный | %bool |
    | `reportFalse` | `predicate` | `—` | обычный | %bool |
    | `reportJoinWords` | `reporter` | `text` | обычный | join %words |
    | `reportLetter` | `reporter` | `text` | обычный | letter %ix of %txt |
    | `reportStringSize` | `reporter` | `number` | обычный | length of %s |
    | `reportTextAttribute` | `reporter` | `text` | обычный | %ta of text %txt |
    | `reportUnicode` | `reporter` | `number` | обычный | unicode of %txt |
    | `reportUnicodeAsLetter` | `reporter` | `text` | обычный | unicode %n as letter |
    | `reportIsA` | `predicate` | `—` | обычный | is %s a %typ ? |
    | `reportVariadicIsIdentical` | `predicate` | `—` | обычный | is %all== ? |
    | `reportTextSplit` | `reporter` | `list` | обычный | split %s by %delim |
    | `reportJSFunction` | `reporter` | `—` | обычный | JavaScript function ( %mult%s ) { %code } |

    > **Примечание по безопасности:** `reportJSFunction` позволяет выполнять произвольный JavaScript-код. SnapCode компилятор должен либо запретить использование этого selector-а без явного разрешения `setting allow_js_function = true`, либо выдавать предупреждение `SC4401: reportJSFunction allows arbitrary JavaScript execution`.
    | `reportTypeOf` | `reporter` | `text` | dev | type of %s |
    | `reportTextFunction` | `reporter` | `text` | dev | %txtfun of %s |
    | `reportCompiled` | `reporter` | `—` | dev | compile %repRing for %n args |

    ### Переменные (`variables`)

    | Selector XML | Тип | Возвращает | Режим | Текст блока |
    |---|---|---|---|---|
    | `doSetVar` | `command` | `—` | обычный | set %var to %s |
    | `doChangeVar` | `command` | `—` | обычный | change %hyperVar by %n |
    | `doShowVar` | `command` | `—` | обычный | show variable %var |
    | `doHideVar` | `command` | `—` | обычный | hide variable %var |
    | `doDeleteAttr` | `command` | `—` | обычный | inherit %shd |

    ### Списки (`lists`)

    | Selector XML | Тип | Возвращает | Режим | Текст блока |
    |---|---|---|---|---|
    | `reportNewList` | `reporter` | `list` | обычный | list %exp |
    | `reportCONS` | `reporter` | `list` | обычный | %s in front of %l |
    | `reportListItem` | `reporter` | `any` | обычный | item %idx of %l |
    | `reportCDR` | `reporter` | `list` | обычный | all but first of %l |
    | `reportListLength` | `reporter` | `—` | dev | length of %l |
    | `reportListAttribute` | `reporter` | `any` | обычный | %la of %l |
    | `reportListContainsItem` | `predicate` | `—` | обычный | %l contains %s |
    | `reportListIsEmpty` | `predicate` | `—` | обычный | is %l empty? |
    | `reportListIndex` | `reporter` | `number` | обычный | index of %s in %l |
    | `doAddToList` | `command` | `—` | обычный | add %s to %l |
    | `doDeleteFromList` | `command` | `—` | обычный | delete %ida of %l |
    | `doInsertInList` | `command` | `—` | обычный | insert %s at %idx of %l |
    | `doReplaceInList` | `command` | `—` | обычный | replace item %idx of %l with %s |
    | `reportNumbers` | `reporter` | `list` | обычный | numbers from %n to %n |
    | `reportListCombination` | `reporter` | `—` | обычный | %mlfunc %lists |
    | `reportConcatenatedLists` | `reporter` | `list` | обычный | append %lists |
    | `reportCrossproduct` | `reporter` | `list` | обычный | combinations %lists |
    | `reportTranspose` | `reporter` | `—` | обычный | transpose %l |
    | `reportReshape` | `reporter` | `any` | обычный | reshape %s to %nums |
    | `reportSlice` | `reporter` | `—` | обычный | slice %l by %nums |
    | `reportMap` | `reporter` | `list` | обычный | map %repRing over %l |
    | `reportAtomicMap` | `reporter` | `list` | dev | $blitz map %repRing over %l |
    | `reportKeep` | `reporter` | `list` | обычный | keep items %predRing from %l |
    | `reportAtomicKeep` | `reporter` | `list` | dev | $blitz keep items %predRing from %l |
    | `reportFindFirst` | `reporter` | `any` | обычный | find first item %predRing in %l |
    | `reportAtomicFindFirst` | `reporter` | `any` | dev | $blitz find first item %predRing in %l |
    | `reportCombine` | `reporter` | `any` | обычный | combine %l using %repRing |
    | `reportAtomicCombine` | `reporter` | `any` | dev | $blitz combine %l using %repRing |
    | `doForEach` | `command` | `—` | обычный | for each %upvar in %l %cla |
    | `doShowTable` | `command` | `—` | dev | show table %l |

    ### Прочее (`other`)

    | Selector XML | Тип | Возвращает | Режим | Текст блока |
    |---|---|---|---|---|
    | `doWarp` | `command` | `—` | обычный | warp %c |
    | `reifyScript` | `ring` | `—` | обычный | %rc %ringparms |
    | `reifyReporter` | `ring` | `—` | обычный | %rr %ringparms |
    | `reifyPredicate` | `ring` | `—` | обычный | %rp %ringparms |
    | `doDeclareVariables` | `command` | `—` | обычный | script variables %scriptVars |
    | `doMapCodeOrHeader` | `command` | `—` | обычный | map %cmdRing to %codeKind %code |
    | `doMapValueCode` | `command` | `—` | обычный | map %mapValue to code %code |
    | `doMapListCode` | `command` | `—` | обычный | map %codeListPart of %codeListKind to code %code |
    | `reportMappedCode` | `reporter` | `text` | обычный | code of %cmdRing |
    | `doPrimitive` | `command` | `—` | обычный | %bool primitive %prim |
    | `doApplyExtension` | `command` | `—` | обычный | extension %ext %mult%s |
    | `reportApplyExtension` | `reporter` | `any` | обычный | extension %ext %mult%s |
    | `reportConnected` | `predicate` | `—` | dev | arduino connected? |
    | `digitalWrite` | `command` | `—` | dev | set digital pin %n to %b |
    | `pwmWrite` | `command` | `—` | dev | set pin %n to value %n |
    | `servoWrite` | `command` | `number` | dev | set servo %n to %s |
    | `reportDigitalReading` | `predicate` | `—` | dev | digital reading %n |

    ## Приложение B. Канонический пример

    ```snapcode
    snapcode 1.0
    target snap "12.2.0"

    project "Round Trip Demo":
        notes "Generated by SnapCode"
        selected_scene "Main"

        scene "Main":
            setting hyper_ops = true
            global var score: number = 0

            stage:
                size 480, 360
                tempo 60

            sprite "Cat":
                position 0, 0
                costume "Cat" from "assets/cat.svg" center (50, 50)
                sound "Meow" from "assets/meow.wav"

                blockdef local command "jump %n" category "motion":
                    input height type number default 30
                    body:
                        primitive "changeYPosition"(height)
                        primitive "doWait"(0.2)
                        primitive "changeYPosition"(-height)

                on green_flag:
                    score = 0
                    repeat 10:
                        move(10)
                        score += 1
                    broadcast("ready")

                on key("space"):
                    custom local "jump %n"(30)
                    say("Jump!", 1)
    ```

    Этот пример использует удобные формы и канонический вызов selector-а одновременно. После lowering оба вида превращаются в одну и ту же Snap IR, а затем сериализуются адаптером 12.2.0.

    ## Приложение C. Инструкция для ИИ

    ```text
    Пиши только на SnapCode 1.0 с target snap "12.2.0".
    Не создавай и не редактируй XML напрямую.
    Используй отступ ровно 4 пробела и расширение .snapcode.
    Предпочитай удобные конструкции языка.
    Если удобной конструкции нет, используй primitive с selector из каталога 12.2.0.
    Не придумывай selector-ы и не используй dev-примитивы без разрешения.
    Для пользовательских блоков сначала создай blockdef, затем вызывай custom.
    Не создавай raw_block/raw_xml для нового кода: эти формы предназначены прежде всего для декомпиляции и сохранения неизвестного XML.
    Перед выдачей проверь области переменных, количество аргументов, тип блока и receiver.
    Если задача требует неподдерживаемого внешнего расширения, явно сообщи об этом вместо выдумывания команды.
    ```

## Инструкция для ИИ №2

```text
Ты пишешь программы на языке SnapCode 1.0.

Используй только нормативный синтаксис SnapCode.
Целевая версия среды: Snap! 12.2.0.

Каждый самостоятельный файл начинай с:

snapcode 1.0
target snap "12.2.0"

Не создавай и не редактируй XML вручную.
Не придумывай selector-ы Snap!.
Не используй Python-функции или JavaScript-функции, если они не описаны в SnapCode.
Не используй dev-примитивы без явного разрешения.

Используй нормативную иерархию:

project "Name":
    scene "Main":
        sprite "Cat":
            on green_flag:
                move(10)

Соблюдай отступ ровно 4 пробела на уровень.
Используй один стиль кавычек.
Проверяй вложенность блоков.
Проверяй количество аргументов.
Проверяй области видимости переменных.

Разрешённые базовые типы:
- int
- str
- any

Если задача не может быть решена доступными возможностями, выведи:

UNSUPPORTED: описание недоступной возможности

Перед выдачей кода проверь:
- заголовок snapcode и target;
- существование проекта и сцены;
- существование спрайта;
- правильность событий;
- правильность отступов;
- количество аргументов;
- существование команд;
- области видимости переменных;
- допустимость циклов и условий;
- отсутствие прямого XML.
```

ИИ должен генерировать только SnapCode. XML создаётся компилятором внутри SnapCode runtime или CLI.
