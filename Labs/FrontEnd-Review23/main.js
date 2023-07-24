function changeBackgroundColor(color) {
    var currColor = document.body.style.backgroundColor;
    // see how to not hard code line 5
    if (currColor == color) {
        document.body.style.backgroundColor = 'lightblue'
    }
    else {
        document.body.style.backgroundColor = color;
    }  
}