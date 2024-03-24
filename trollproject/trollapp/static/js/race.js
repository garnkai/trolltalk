/*My idea for the text logic is that, when you input a letter, the value will 
instantly change back to the original text value, but at the current index change the colour

Once type an incorrect character, the rest of the letters should be red or incorrect too
To do this, a mistake bool will probably be used to keep track is user has made a 
mistake yet or not*/
            
const textBoxElement = document.querySelector(".textBox");

// When the textbox goes out of focus when user clicks out of it, refocus it
// So that the user can continue typing on the textbox
textBoxElement.addEventListener("blur", () => {
    textBoxElement.focus();
});

/* Function handle input is called everytime the textbox has an oninput event,
so everytime 
*/

function handleInput(text) {
    //console.log("textInput: " + text);
    const origText = "Hello this is a typing test.";
    const typedTextElement = document.getElementById("typedTextContent");
    const cursorElement = document.getElementById("cursor");

    /* Set the visible typed text to blank to start, then loop through
    all the characters in the original text.
    Spawn or create a span text element with the current character in the loop
    If the character typed in the textbox is correct, then set the visible font
    to correct (green), add the spans to the span/div*/
    typedTextElement.innerHTML = "";
    let mistake = false;
    for (let i = 0; i < origText.length; i++) {
        const charSpan = document.createElement("span");
        charSpan.textContent = origText.charAt(i);

        if (i >= text.length) {
            // default text (black), has not been typed yet
            charSpan.classList.add("default"); // green
        } 
        else {
            // If a mistake happened, the following text is red
            if (mistake) {
                charSpan.classList.add("mistake");
            } 
            else {
                if (i < text.length && origText.charAt(i) === text.charAt(i)) {
                    charSpan.classList.add("correct"); // green
                }
                else {
                    // Set mistake to the index
                    mistake = true;
                    charSpan.classList.add("mistake");
                }
            }
        }

        typedTextElement.appendChild(charSpan);

        // Check for win
        if (text.length == origText.length && !mistake) {
            // Typing is over, hide typingContent show endContent
            document.querySelector("#typingContent").classList.add("hidden");
            //document.querySelector("#typingContent").remove();
            document.querySelector("#endContent").classList.remove("hidden");
        }
    }

    const cursorPosition = text.length * 15; 
    cursorElement.style.left = `${cursorPosition}px`;
}

// Call the function once on start to reset everything
handleInput("");



