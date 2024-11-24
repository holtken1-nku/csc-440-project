My original plan for the frontend was to write it in a language called Elm.
Elm is a functional programming language that transpiles into Javascript and 
prides itself on the guarantees that come from being purely function. The
benefits of Elm are:

- **No runtime errors**. Due to the guarantees of being strongly-typed and of
  pure functions, the compiler catches essentially all runtime errors. One 
  aspect of it that amazes me is that if you have a conditional that doesn't
  cover all potential branches then the program won't compile and the compiler
  will yell at you.

  For example:

  ```elm
  type Food
      = Pizza
      | Salad

  foodToString x =
    case x of
      Pizza ->
        "Pizza"
      Salad ->
        "Salad"
  ```

  The above example would compile fine. But, the below one wouldn't:

  ```elm
  type Food
      = Pizza
      | Salad
      | Pie

  foodToString x =
    case x of
      Pizza ->
        "Pizza"
      Salad ->
        "Salad"
  ```

  The reason this one wouldn't compile would be because if foodToString was 
  supplied Pie then there's no branch to handle it so it'd cause a runtime error.


- **Helpful Error Messages.**

  The error message that you'd receive above is this:

  ```
  Detected problems in 1 module.
  -- MISSING PATTERNS ----------------------------------------------- src/Main.elm

  This `case` does not have branches for all possibilities:

   9|>    case x of
  10|>      Pizza ->
  11|>        "Pizza"
  12|>      Salad ->
  13|>        "Salad"

  Missing possibilities include:

      Pie

  I would have to crash if I saw one of those. Add branches for them!

  Hint: If you want to write the code for each branch later, use `Debug.todo` as a
  placeholder. Read <https://elm-lang.org/0.19.1/missing-patterns> for more
  guidance on this workflow.
  ```

  Of all the programming languages I've used, Elm's error messages have been the
  most useful.


- **Very Opinionated.** This is debatable if it's truly a perk, but in Elm it's
  sort of been decided that there's usually a best way to do things. It makes it
  really easy to approach problems. 


- **"The Elm Architecture"**. The way that Elm works is you create an additional
  model, that's fed into a view function. It's the view function that lays out
  the general structure of the program and, if your program is dynamic, then the
  view function will contain elements (like html buttons) that create events. 
  When a user interacts with, say, a button then it'll send the event to the 
  update function and the update function can update the model that is then fed
  back into the view function.




I ended up putting a decent amount of time and work into Elm. I read a lot of
Richard Feldman's ["Elm in Action"](https://www.amazon.com/Elm-Action-Richard-Feldman-ebook/dp/B09781K9CK) 
out of fear towards Elm because my main experience with Function Programming was
trying to learn Haskell which was incredibly hard and confusing.

After awhile I got tired of reading him lay out a program that didn't seem very
similar to my needs so, I start just writing the Elm. When using the elm/html
library it's actually not very different than writing regular html:

```elm
div 
  [ class "header" ]
  [ text "CSC 440 Project"
  , button [ id "menu", onClick BlowUpTheWorld ]
  ]
```

The main difference is that the strong guarantees of Elm makes it more difficult
to make syntactical mistakes than regular HTML.

At first my plan was to use Elm in place of HTML and Javascript, but still use
CSS, but there's an elm library called **elm-ui** that allows you to do that in
Elm as well. It's an incredibly convenient library that allows you to things that
would be pretty complex (and require a lot of divs in html/css) very easily. For
example:

```elm
row [ height fill, width fill ] 
  [ column [ height fill, width (fillPortion 1) ] 
      [ el [ centerX, centerY ] 
          [ text "1" ]
      , el [ centerX, centerY ] 
          [ text "3" ]
      ]
  , column [ height fill, width (fillPortion 1) ] 
      [ el [ centerX, centerY ] 
          [ text "2" ]
      , el [ centerX, centerY ] 
          [ text "4" ]
      ]
  ]
]
```

If I wrote that correctly, it would result in this sort of arrangement:

```
┌──────────┐ 
│          │  
│  1    2  │ 
│          │     
│          │     
│  3    4  │     
│          │     
└──────────┘
```

The area would be divided evenly into four regions with the numbers centered. It
would be a massive chore in css so it being so easy with elm-ui was a breeze.

After getting the structure of the program together I started looking for how to
solve the actual problem of the project: what libraries in elm are there to display
the data?

It only took a short amount of time before I stumbled upon [**elm-charts.**](https://www.elm-charts.org/)
(The website is absolutely gorgeous, I really recommend checking it out).

I installed it into my project (using Elm requires you to setup projects), then
other classes got me too busy to do much of anything with it for awhile.

When I got back to it, I tried to integrate a sample chart into my frontend and
figured out how to navigate the hell that are type systems (you really have to
think about the types a function takes and returns and how to translate between
types if need be, but I digress...). 

After messing around with it for a few hours across a few days. I stumbled upon
an [issue](https://github.com/terezka/elm-charts/issues/129) on the elm-charts 
github that mentioned my specific issue from about 5 months ago mentioning my
exact issue. It has yet to get a response and the person seems significantly more
experienced than I am.

That's one of the downsides to Elm I think. It's got a much smaller userbase than
something like Javascript or, say, React so there's not as many projects and also
less people using it to work out bugs when using libraries together. Also, Elm
hasn't had a release since 2019 which probably doesn't encourage people to get into
it or maintain enthuasism for it.

I don't have very much time left, I'd given up given on Elm prior to writing this
and it's the Saturday night before. I could always go through and rewrite the
Elm program without using **elm-ui**, but I think, instead, I'm gonna try to use
a solution called Grafana. 

  
