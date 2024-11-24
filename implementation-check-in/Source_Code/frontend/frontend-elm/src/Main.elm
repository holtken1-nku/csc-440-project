module Main exposing (main)

import Browser

-- All of these imports are related to elm-ui. It's a replacement for using CSS 
-- for styling, and, on top of just never having to leave Elm, it makes vertical
-- alignment trival (which is something kind of complicated in css).
import Element exposing (..)
import Element.Background as Background
import Element.Border as Border
import Element.Events exposing (..)
import Element.Font as Font
import Element.Input as Input
import Element.Region exposing (description)

-- If not using elm-ui you'd typically importal all of Html and use its functions
-- to construct your application (e.g. Html.div, Html.button, etc.), but the
-- Element module has replacements.
import Html exposing (Html)

-- This is for the library elm-charts. It's meant to be an easy way to make 
-- beautiful charts in elm. The reason using Elm didn't end up being feasible
-- was because elm-charts and elm-ui didn't seem compatible and elm-charts seems
-- required for our project.
import Chart as C
import Chart.Attributes as CA

-- These would be for pulling from the json api that Nathan setup.
import Http
import Json.Decode exposing (Decoder, map4, field, int, string)

-- These are the events that can be triggered by user interaction.
type Msg
    = ChangePage Page
    | CollapseSidebar

-- These are the different pages that our dashboard has.
type Page
    = Teams
    | Standings
    | Competitions
    | Matches

-- A list of the different pages to be used by the generateSidebarButtons function
-- in order to create all the sidebar buttons.
pages : List Page
pages =
    [ Teams
    , Standings
    , Competitions
    , Matches
    ]

-- Declaration of the different color values used in the program so that they're
-- easy to change.
color =
    { accent = rgb255 0xFF 0xC7 0x2C
    , white = rgb255 0xFF 0xFF 0xFF
    , black = rgb255 0x00 0x00 0x00
    }

-- This just lays out the structure of the model. A type alias just defines a
-- type based on other existing data types. All of the values in model are used
-- to track/manipulate the state of the frontend.
type alias Model =
    { selectedPage : String
    , content : String
    , isSidebarVisible : Bool
    }

-- This is the initial state of the application when the webpage loads.
initialModel : Model
initialModel =
    { selectedPage = "FIFA"
    , content = ""
    , isSidebarVisible = False
    }

-- This is essentially just a toString function for my custom type Page. It's
-- used to generate the text on the sidebar buttons. One of my main desires in
-- writing this frontend was to try to hardcode as little as possible.
pageToString : Page -> String
pageToString page =
    case page of
        Teams ->
            "Teams"

        Competitions ->
            "Competitions"

        Standings ->
            "Standings"

        Matches ->
            "Matches"


-- depending on the value of the model's isSidebarVisible variable, this function
-- either returns the sidebar or an empty element.
toggleSidebar : Bool -> Element Msg
toggleSidebar isSidebarVisible =
    if isSidebarVisible then
        sidebarPanel
    else
        el [] none

-- generates the buttons that go on the sidebar based on the pages list above.
generateSidebarButton: Page -> Element Msg 
generateSidebarButton page =
    Input.button [ width fill, padding 5, Font.size 50 ]
        { onPress = Just (ChangePage page) -- this is the button action 
        , label = text (pageToString page) -- this is the button text.
        }

-- Generates the sidebar full of buttons. It uses List.map in order to apply the
-- values in the pages list to the generateSidebarButton, spitting out a list of
-- buttons in return.
sidebarPanel : Element Msg
sidebarPanel = 
    column 
        [ height fill, padding 5, Background.color color.accent ]
        (List.map generateSidebarButton pages)

    

-- This is the header at the top of the page (visible in screenshots).
-- The title in the middle of the header changes based on what page you're on
-- and updates based on the model's selectedPage variable. It also has a button
-- that toggles the sidebar.
header : String -> Element Msg
header title =
    row [ width fill, Background.color color.accent, Font.size 50, Font.center, padding 8 ] 
        [ Input.button [ width <| maximum 100 fill ] 
            { onPress = Just CollapseSidebar
            , label = text "☰"
            }
        , paragraph []
            [ text title ]
    ]

-- This would be the content of the main panel (the empty white area in the 
-- screenshot). the C.____ and CA.____ elements come from elm-charts. When used
-- on their own they work perfectly fine, but in conjunction with the elm-ui 
-- elements they just show up as pure white. 
mainPanel : String -> String -> Element msg
mainPanel content selectedPage =
        html (C.chart 
            [ CA.height 300 , CA.width 300 ]
            [ C.xAxis []
            , C.xTicks []
            , C.xLabels []
            , C.yAxis []
            , C.yTicks []
            , C.yLabels []
            ]
        )

        
-- This is the function that defines the layout of the program. 
view : Model -> Html Msg
view model =
    layout [ width fill, height fill ] <|
        column [ width fill, height fill ] 
        [ header model.selectedPage
        , row [ height fill ] 
            [ toggleSidebar model.isSidebarVisible        -- toggles if the sidebar is visible
            , mainPanel model.content model.selectedPage  -- changes the content of the main panel
            ]
        ]

            
-- when a button is clicked the event tied to it (and the current state of the 
-- model) is supplied to this function. It goes through the case statement, then
-- updates the model accordingly and the view function is reran.
update : Msg -> Model -> Model
update msg model =
    case msg of
        ChangePage page ->
            { model | selectedPage = pageToString page, content = "", isSidebarVisible = False }
        CollapseSidebar ->
            { model | isSidebarVisible = (not model.isSidebarVisible) }

-- the main program loop
main : Program () Model Msg 
main =
    Browser.sandbox
        { init = initialModel
        , view = view
        , update = update
        }
