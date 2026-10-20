# Сценарий и дизайн-проект интерактивной презентации (5 слайдов / 5 спикеров)

> **Концепция проекта:** Интерактивная командная презентация в стиле «геймифицированного кейса» (2 уровня игры + разбор стратегии + профессиональная эскалация + интерактивный финал).
> 
> **Технический стек:** 3D-визуализация на **Three.js** с автономными зацикленными анимациями (**Zero-Click Looping Ambient Animations**). Спикерам не нужно отвлекаться на кликеры во время речи — сцена живет сама, адаптируясь под живое выступление.

---

## 📋 Карта презентации и распределение ролей

| № | Слайд | Спикер | Ключевая тема | Формат и механика |
|---|---|---|---|---|
| **1** | **Level 1: The Missing Teammate** | **Спикер 1** | Запуск игры, кейс «игнор в 14:00», 3 правила сообщения | Интерактив с залом (задание на 5 минут, 10 очков) |
| **2** | **Level 2: Emotional Teammate** | **Спикер 2** *(+ Спикер 1)* | Реакции на стресс: Sarcastic, Dramatic, Stressed | Мини-сценка / живой диалог на фоне 3D-арены |
| **3** | **Core Strategy: Deadline & Backup** | **Спикер 3** | Дедлайн 17:00 и распределение 3 пустых слайдов (План Б) | Разбор внутренней командной стратегии |
| **4** | **Escalation: Informing the Lecturer** | **Спикер 4 (Вы)** | Профессиональное обращение к преподавателю без обвинений | Этика эскалации: факты, усилия команды, план Б |
| **5** | **Roadmap & Open Discussion** | **Спикер 5** | Итоговые 3 шага, формула успеха, вопрос аудитории | Интерактивное голосование / обсуждение с классом |

---

## ⚙️ Технический стандарт сцены (Three.js Architecture)

1. **Принцип «Zero-Click Looping»:**
   * Каждое переключение слайда осуществляется **единственным нажатием** (`Space` / `ArrowRight`).
   * **0.0s – 2.0s (Staggered Reveal):** Плавный перелет камеры к новой тематической станции, всплытие HUD-панелей и сборка 3D-композиции.
   * **2.0s+ (Infinite Ambient Loop):** Автономная динамическая сцена на синусоидах и частицах (`clock.getElapsedTime()`). Спикер может говорить 30 секунд или 3 минуты — визуал выглядит идеально синхронизированным без таймингов и ручных переключений.
2. **Опциональный Web Audio API (Mic Reaction):**
   * Подключение микрофона ноутбука к шейдерам или масштабу объектов: сцена мягко резонирует в такт голосам спикеров при живом выступлении.

---

## Слайд 1: Level 1 — The Missing Teammate (Interactive Mission)

* **👤 Спикер:** Спикер 1  
* **🎯 Задача:** Задать энергичный темп, объявить начало игры (2 уровня с баллами), погрузить аудиторию в проблемную ситуацию и объявить задание на 5 минут.  
* **⏱️ Примерное время:** 2.5 – 3 минуты  

### 🖥️ Текст на слайде (HUD & On-Screen Content)

* **Заголовок:** `LEVEL 1: The Missing Teammate (10 Points | 5 Minutes)`
* **The Situation:**
  * Three slides are completely empty.
  * Your teammate read the message at **2:00 PM**. Still no reply.
* **Your Mission — Write a group text to request missing work:**
  1. **Be firm but respectful** (not aggressive, not overly apologetic).
  2. **Give a clear deadline** (exact day & time, never say "ASAP").
  3. **Make a backup plan** (clearly state who steps in if missed).
* **Comparison:**
  * ❌ **Bad Example:** *“Are you done yet? Hurry up.”*
  * ✅ **Good Example:** *“Hi Sam, we still need slides 4 to 6. Could you send them by Thursday 6 PM? If that’s hard, tell me today, and I’ll take slide 6 myself. Thanks!”*
* **Fun Twist:** *“We will pick the most awkward message anonymously and upgrade it live on screen!”*

### 🎨 3D-сцена и визуализация (Three.js)

* **Вход (0.0s – 1.5s):** Камера подлетает к парящей изометрической платформе.
* **Центр сцены:** 3D-модель смартфона с эффектом матового стекла. На экране отображается чат с непрочитанной задачей и крупным пульсирующим бейджем `Read at 2:00 PM` с двойной синей галочкой.
* **Справа:** Три голографические карточки с иконками правил:
  * 🛡️ Щит — *Respectful & Firm*
  * ⏰ Часы — *Exact Deadline*
  * 🪂 Парашют — *Backup Plan*
* **Внизу:** Два контрастных неоновых блока: красный (`Bad ❌`) и изумрудный (`Good ✅`).
* **Фоновый луп (Ambient Loop):** В углу медленно вращается объемный голографический таймер `05:00` с парящими вокруг светящимися искрами.

### 🎙️ Речь Спикера 1 (Script)

> “Hello, everyone! Welcome. Today we’re going to play a game about one crucial real-life skill: how to handle a difficult teammate.
> 
> There are two levels, and you will earn points in each one. Are you ready? Let’s start with **Level 1**.
> 
> Level 1 is called *The Missing Teammate*. Imagine a group project. Three slides are still empty. The person in charge has read your messages. Look at the screen: ‘Read at 2:00 PM.’ They’ve seen it, but they never replied. You might feel frustrated. You might want to type: ‘Why are you ignoring me?’ But the project still has to get done. So, what do you do?
> 
> You have 5 minutes, and this challenge is worth 10 points. Your mission: write a group text to request the missing work. Here are three golden rules:
> * **One:** Be firm but respectful. If you sound angry, people become defensive. If you’re too soft, you get ignored.
> * **Two:** Give a clear deadline. Never write ‘as soon as possible.’ Give an exact day and time.
> * **Three:** Make a backup plan. Clearly state who will step in if the deadline is missed.
> 
> Look at the bad example on screen: *‘Are you done yet? Hurry up.’* It creates hostility, offers no clear deadline, and has no backup plan.
> Now look at the good one: *‘Hi Sam, we still need slides 4 to 6. Could you send them by Thursday 6 PM? If that’s hard, tell me today, and I’ll take slide 6 myself. Thanks!’* It is respectful, precise, and proactive.
> 
> Here’s the fun twist: I will pick the most awkward submission anonymously, and we’ll upgrade it live together! Your 5 minutes start now!”

---

## Слайд 2: Level 2 — Choices & Emotional Role Play

* **👤 Спикер:** Спикер 2 *(при участии Спикера 1 в роли эмоционального тиммейта)*  
* **🎯 Задача:** Разобрать дилемму выбора (ждать или действовать) и продемонстрировать хладнокровные профессиональные ответы на три острых типа эмоциональной реакции.  
* **⏱️ Примерное время:** 2 – 2.5 минуты  

### 🖥️ Текст на слайде (HUD & On-Screen Content)

* **Верхний заголовок (HUD):** `LEVEL 2: Handling Emotional Reactions (Live Role Play)`
* **Дилемма:**
  * *Wait for reply?* ➔ Wastes valuable time.
  * *Set deadline & backup plan?* ➔ Keeps project moving safely.
  * *Core question:* How to de-escalate tension without creating conflict?
* **Нижняя статус-панель (Неоновые бейджи):**  
  `[ 🎭 Sarcastic ]` + `[ 😱 Dramatic ]` + `[ 😰 Stressed ]` ➔ **`[ 🛡️ Calm & Supportive Response ]`**

### 🎨 3D-сцена и визуализация (Three.js — Концепт «Две Голографические Головы»)

* **Композиция:** В пространстве друг напротив друга парят два детализированных 3D-бюста:
  * **Слева — «The Exploding Teammate» (Хаос / Эмоции):** Угловатая low-poly модель, подсвеченная изнутри пульсирующим огненным неоном (`#ff2a5f` / `#ff7b00`). Область челюсти и рта совершает резкие рваные колебания, над головой парят искры и мини-символы шторма/молнии ⚡.
  * **Справа — «The Calm Professional» (Самообладание):** Плавный скульптурный бюст из полупрозрачного стекла и бирюзового неона (`#00f0ff` / `#00ffaa`). Вокруг него медленно и гармонично вращаются орбитальные кольца гироскопа, а звуковая волна у висков пульсирует плавной синусоидой.
* **Центральный эффект — «Soundwave Bridge» (Мост трансформации):**
  * От левой головы исходят дерганые красные шумовые волны.
  * В центре сцены они проходят сквозь преломляющую стеклянную 3D-призму и **на лету сглаживаются в чистый бирюзовый поток**, входящий в правую голову.
  * Это метафора деэскалации: спокойствие поглощает агрессию и трансформирует ее в конструктив.
* **Звуковая реакция (опционально):** При живой речи через микрофон головы и волна между ними оживают в такт голосам выступающих.

### 🎙️ Речь Спикера 2 (+ мини-сценка со Спикером 1)

> **Спикер 2:**  
> “Imagine that you are working on a group presentation with several classmates. Everyone has their own responsibilities, but one teammate has completely disappeared. You sent them a message at 2:00 PM, they read it, but they never replied. Now, three slides are still empty, and the deadline is getting dangerously close.
> 
> In this situation, you face a critical dilemma. You could just wait for a reply, but this wastes valuable preparation time. Alternatively, you could send a structured message with a firm deadline and prepare a backup plan. The real challenge is: how do we solve this problem without triggering interpersonal conflict, while still guaranteeing the work gets done?
> 
> Now, welcome to **Level 2**. Imagine your teammate finally replies—but they are highly emotional! Let’s see how to defuse three different emotional states live.”
> 
> *(Живой диалог: Спикер 1 отыгрывает эмоцию, Спикер 2 отвечает спокойно)*
> 
> * **Спикер 1 *(Sarcastic — с едким сарказмом)*:**  
>   *“Oh great, keep spamming me! Sure, I guess I’m the only person in this university who isn't doing anything!”*
> * **Спикер 2 *(Calm response 1)*:**  
>   *“I understand you feel overwhelmed, and it’s not our intention to make you feel singled out. Let’s focus on the remaining tasks and finish them together.”*
> 
> * **Спикер 1 *(Dramatic — с паникой и драмой)*:**  
>   *“Everything is completely ruined! We’re never going to finish on time, and we’re going to fail the entire course!”*
> * **Спикер 2 *(Calm response 2)*:**  
>   *“Don’t worry, take a breath. We have plenty of time if we stay organized. We will solve this step-by-step and deliver a great presentation.”*
> 
> * **Спикер 1 *(Stressed — в состоянии перегруза)*:**  
>   *“I have three exams tomorrow and zero sleep, I literally cannot touch these slides right now!”*
> * **Спикер 2 *(Calm response 3)*:**  
>   *“I hear you, stress is tough. Let’s look at your part: tell us what’s drafted, and we’ll redistribute the rest. You’re not alone in this.”*

---

## Слайд 3: Deep Dive — Setting a Deadline & Preparing a Backup Plan

* **👤 Спикер:** Спикер 3  
* **🎯 Задача:** Разобрать детальную механику двух ключевых шагов: выставление жесткого дедлайна (17:00) и распределение работы по «Плану Б» с акцентом на факты, а не на полировку дизайна.  
* **⏱️ Примерное время:** 2 минуты  

### 🖥️ Текст на слайде (HUD & On-Screen Content)

* **Заголовок:** `Core Strategy: Clear Deadlines & Backup Plans`
* **Column 1 — Step 2: Set a Clear Deadline (5:00 PM):**
  * Communicate professionally instead of spamming or expressing anger.
  * Gives the teammate an honest window to explain difficulties or ask for help.
  * **Why 5:00 PM?** Leaves critical buffer time to review content and rehearse as a team.
  * *Guiding principle:* Being polite never means compromising on team accountability.
* **Column 2 — Step 3: Activate a Backup Plan (If Empty at 5:00 PM):**
  * Remaining members divide the 3 missing slides equally (1 part per person).
  * **Rule of Priority:** Focus on core research and data first — styling comes second.
  * Run a final joint review to ensure smooth narrative flow and stylistic unity.
  * **Outcome:** Prevents panic, saves time, and keeps the presentation on schedule.

### 🎨 3D-сцена и визуализация (Three.js)

* **Двухколоночный визуал:**
  * **Слева (Дедлайн 17:00):** Светящийся 3D-циферблат с акцентными стрелками на 17:00. Под ним — парящий интерактивный чек-лист с зелеными галочками (`[✓] Slide Review`, `[✓] Team Rehearsal`).
  * **Справа (План Б):** Три полупрозрачных прямоугольника слайдов. Каждые 6–8 секунд запускается плавный зацикленный пинг-понг луп (`Ping-Pong Loop`): карточки разлетаются к трем иконкам участников, наполняются светящимися строками данных и синхронно выстраиваются в единый аккуратный ряд.
  * **Сверху:** Неоновая плашка-манифест: `Content First > Design Second`.

### 🎙️ Речь Спикера 3 (Script)

> “Now let’s look deeper at the core operational strategy on Slide 3: setting a firm deadline and executing a reliable backup plan.
> 
> **First, setting a clear deadline.** When a teammate goes silent, sending dozens of frantic texts or venting anger solves nothing. Instead, we must communicate with professional clarity. We send a formal update stating exactly which three slides are missing and establish a firm deadline—specifically, **5:00 PM**. 
> 
> Why 5:00 PM? Because setting the deadline right before class leaves no margin for error. A 5:00 PM cutoff gives our teammate a fair window to submit their work or communicate an emergency, while still leaving the team enough buffer time to check the content and run a full rehearsal. Remember: being respectful does not mean avoiding accountability.
> 
> **Second, preparing the backup plan.** In university and professional projects, things rarely go 100% according to plan. That is why proactive teams never rely on luck. If 5:00 PM arrives and those slides remain blank, the backup plan activates instantly. The remaining members split the three slides equally—one concise section per person.
> 
> Crucially, we follow the rule shown on screen: **focus on core content first, not visual decoration**. Gather the facts, ensure arguments are clear, and unify the typography. Having complete, structured information always matters more than fancy animations. A structured backup plan eliminates panic and ensures the team stands united tomorrow.”

---

## Слайд 4: Professional Escalation — Informing the Lecturer

* **👤 Спикер:** Спикер 4 (Вы)  
* **🎯 Задача:** Показать зрелый и этичный алгоритм эскалации: как правильно уведомить преподавателя, если участник сорвал дедлайн, не скатываясь в токсичные жалобы и перекладывание вины.  
* **⏱️ Примерное время:** 2 минуты  

### 🖥️ Текст на слайде (HUD & On-Screen Content)

* **Заголовок:** `Next Step: Informing the Lecturer Professionally`
* **When to Contact the Lecturer:**
  * Only **after** direct communication attempts and a reasonable deadline have passed.
  * When the absence directly threatens the academic deliverable of the whole team.
* **The 3-Point Professional Message:**
  1. **State the facts objectively:** 3 specific slides remain incomplete.
  2. **Demonstrate team initiative:** Messages were sent, and a 5:00 PM cutoff was established.
  3. **Present the proactive solution:** The team activated a backup plan to protect project quality.
* **Our Core Mindset (Zero-Blame Culture):**
  * ❌ *Not* to complain, punish, or humiliate the teammate.
  * ✅ To provide an honest progress update, protect grading fairness, and ask for guidance.
* **Golden Rule:** *Resolve issues internally whenever possible, but never hesitate to seek professional guidance when necessary.*

### 🎨 3D-сцена и визуализация (Three.js)

* **Центральный элемент:** Голографический терминал отправки сообщения (интерфейс университетского Email / Teams). В письме мягким неоновым светом подсвечены три структурных блока:
  * `[ 1. Objective Facts ]` ➔ `[ 2. Action Taken ]` ➔ `[ 3. Backup Plan Active ]`
* **Анимация эскалации:** От нижней платформы команды вверх к стилизованной 3D-иконке преподавателя (академическая мантия / кафедра) непрерывно течет ровный световой поток частиц золотисто-лазурного цвета, символизируя прозрачность коммуникации.
* **Сбоку:** Контрастный аналитический блок: `Toxic Complaining ❌` против `Objective Escalation & Guidance ✅`.

### 🎙️ Речь Спикера 4 (Ваша речь — Script)

> “Now I will present Slide 4, which covers the most delicate yet necessary step in professional teamwork: informing the lecturer if the issue persists and begins to impact the group.
> 
> Reaching out to a supervisor or professor should never be an emotional first reaction. We must always make genuine internal efforts first—reaching out directly and offering reasonable deadlines. However, if the deadline passes and there is still total silence, escalating the matter becomes a matter of professional responsibility.
> 
> When communicating with the lecturer, we follow three objective steps:
> * First, we state the bare facts without drama: three slides are currently missing.
> * Second, we show that the team took initiative: we reached out repeatedly and set a clear 5:00 PM deadline.
> * Third, we demonstrate competence: we inform the lecturer that our backup plan is already active to safeguard presentation quality.
> 
> It is vital to emphasize our mindset: **our goal is never to blame, complain, or embarrass our teammate**. Unforeseen emergencies happen. Instead, our objective is to provide complete transparency, ensure fair grading, and seek academic advice if needed.
> 
> As our golden rule states: always strive to solve problems within your team first, but never be afraid to communicate professionally with your supervisor when project success is on the line.”

---

## Слайд 5: Summary — Three Steps to Save the Team & Open Discussion

* **👤 Спикер:** Спикер 5  
* **🎯 Задача:** Подвести целостный итог всего выступления, повторить алгоритм трех шагов и вовлечь зал в открытую дискуссию финальным вопросом.  
* **⏱️ Примерное время:** 2 – 2.5 минуты  

### 🖥️ Текст на слайде (HUD & On-Screen Content)

* **Заголовок:** `Summary: How to Handle the "Missing Teammate" Crisis`
* **Scenario Recap:**
  * Message read at **2:00 PM**, zero reply, **3 slides empty**, deadline approaching.
* **The 3-Step Professional Roadmap:**
  * **1. Communicate & Set a Deadline:** Send a respectful group text with a firm **5:00 PM** cutoff so expectations are crystal clear.
  * **2. Activate the Backup Plan:** If slides remain empty at 5:00 PM, redistribute the workload and finish the project together.
  * **3. Inform the Lecturer Professionally:** If unresolved, report the situation factually without assigning personal blame.
* **The Success Formula:**  
  `Clear Communication + Realistic Deadlines + Prepared Backup = Stress-Free Delivery 🎯`
* **💬 Open Discussion Question:**  
  *“Which of these three options would YOU personally rely on first, and why?”*

### 🎨 3D-сцена и визуализация (Three.js)

* **Композиция «Три Монолита»:** На просторной футуристичной платформе возвышаются три световых обелиска, соединенных бегущей неоновой линией таймлайна:
  * Монолит 1: Иконка сообщения + бейдж `5:00 PM Deadline`.
  * Монолит 2: Иконка команды + бейдж `Backup Plan & Equal Distribution`.
  * Монолит 3: Иконка академической шапочки + бейдж `Objective Guidance`.
* **Финальный акцент:** В нижней трети экрана мерцает крупный широкоформатный баннер с акцентным вопросом к залу:  
  **«Which option would you choose first, and why?»**
* **Фоновый луп:** Монолиты медленно парят над платформой с мягким градиентным свечением, готовые к интерактивному ответу аудитории.

### 🎙️ Речь Спикера 5 (Script)

> “To bring our presentation to a close on Slide 5, let’s bring together the complete framework for resolving *The Missing Teammate* crisis.
> 
> Recall where we started: an urgent group project, three empty slides, a message read at 2:00 PM with zero response, and time slipping away. Instead of succumbing to panic or frustration, we apply our three-step roadmap:
> 
> * **Step 1: Communicate and set a deadline.** Send a polite, structured message with an unambiguous deadline of 5:00 PM. This gives the teammate a fair opportunity while establishing team accountability.
> * **Step 2: Activate your backup plan.** If 5:00 PM passes without a response, the remaining team members divide the three slides and focus on solid information first.
> * **Step 3: Inform the lecturer calmly.** If the problem persists, deliver an objective, blame-free briefing to your instructor, outlining the facts, the efforts made, and the active backup solution.
> 
> In conclusion: proactive communication, strict deadlines, and a solid backup plan will guarantee a successful presentation without unnecessary interpersonal conflict.
> 
> Now, we turn the floor over to you: take a moment to reflect on your own project experiences—**which of these options would YOU choose first in this situation, and why?**
> 
> Thank you for your attention!”

---

## 💡 Памятка для команды перед выступлением

```
[Space / Right Arrow] ➔ Плавный переход к следующему слайду (2.0s)
[Никаких кликов во время речи] ➔ Все 3D-диорамы зациклены в Infinite Ambient Loop
[Живая речь] ➔ Спикеры говорят в естественном темпе, опираясь на тезисы слайда
```

1. **Единый визуальный стиль:** Все 5 слайдов выдержаны в темной неоновой кибер-стилистике с акцентными цветами (`#00f0ff` Cyan / `#ff2a5f` Magenta / `#ffaa00` Amber).
2. **Безупречная передача слова:** Спикер 1 запускает интригу, Спикер 2 показывает живую сценку, Спикер 3 дает детальные инструкции, Спикер 4 (Вы) проводит зрелую эскалацию, Спикер 5 красиво замыкает круг и активирует аудиторию.
3. **Готовность к вопросам:** Обратите внимание на открытый вопрос в конце — Спикер 5 может передать микрофон любому желающему из зала или преподавателю.