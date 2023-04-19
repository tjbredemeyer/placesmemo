$(document).on('click', 'td.editable', function() {
    console.log('loaded editable.js');
    // Check if cell is editable
    if ($(this).hasClass('editable')) {
        // Get the current cell text
        var cellText = $(this).text().trim();

        // Get the width of the cell
        var cellWidth = $(this).outerWidth();
        
        // Create an input field with the cell text as the value
        var inputField = $('<input>').attr({
            'type': 'text',
            'class': 'form-control',
            'value': cellText
        }).css('width', cellWidth);;

        // Replace the cell text with the input field
        $(this).html(inputField);
        
        // Change class from 'editable' to 'editing'
        $(this).removeClass('editable').addClass('editing');
        
        // Focus on the input field
        inputField.focus();
        var val = inputField.val();
        inputField.val('');
        inputField.val(val);

        inputField.on('focus', function() {
            var val = $(this).val();
            $(this).val('').val(val);
          });
        
        // Convert back to a table cell on blur
        inputField.on('blur keypress', function(e) {
            if (e.type === 'blur' || e.keyCode === 13) {
                // Change class from 'editing' to 'editable'
                $(this).parent().removeClass('editing').addClass('editable');
        
                // Get the new input value
                var inputValue = $(this).val().trim();
        
                // If the new input value is not empty and is different from the original cell text, update the cell
                if (inputValue !== cellText) {
                    $(this).parent().text(inputValue);
                    // Code to save to database can go here
                } else {
                    $(this).parent().text(cellText);
                }
            }
        });
    };
});


