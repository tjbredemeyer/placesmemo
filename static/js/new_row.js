$(document).ready(function() {
    console.log('loaded new_row.js');
    // Handle add new place button click
    $('#add-new-place').click(function() {
        console.log('add new place button clicked')
        // Clone the last row in the table
        var newRow = $('table tbody tr:last').clone();

        // Clear the values in the form fields
        newRow.find('input[type="text"]').val('');

        // Change the name attributes of the form fields to make them unique
        var newRowId = $('table tbody tr').length;
        newRow.find('input').each(function() {
            var nameAttr = $(this).attr('name');
            $(this).attr('name', nameAttr.replace('-0-', '-' + newRowId + '-'));
        });

        // Clear the content of the first cell and convert it to an input box
        newRow.find('td:first').empty().append($('<input>').attr({
            'type': 'text',
            'class': 'form-control',
            'value': ''
        }));

        // Focus on the input box
        newRow.find('td:first input').focus();

        // Insert the new row after the last row
        $('table tbody tr:last').after(newRow);

        // Scroll to the bottom of the table
        $('html, body').animate({scrollTop: $(document).height()}, 'slow');
    });
});
