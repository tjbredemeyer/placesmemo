$(document).ready(function() {
    console.log("Script loaded");

    // Listen for editing events on table cells
    $('table td.editable').on('blur', function() {
        var cell = $(this);
        var place_id = cell.closest('tr').data('place-id');
        var field_name = cell.data('field-name');
        var field_value = cell.text();

        // Send an AJAX request to update the cell value
        $.ajax({
            url: '/edit-place/',
            type: 'POST',
            data: {
                'place_id': place_id,
                'field_name': field_name,
                'field_value': field_value
            },
            success: function(response) {
                // Update the cell value on success
                cell.text(field_value);
            },
            error: function(xhr, status, error) {
                // Handle any errors that occur during the AJAX request
                console.error(error);
            }
        });

        console.log("Save button clicked");
    });

    // Listen for tag input events
    $('table td.tags input').on('blur', function() {
        var input = $(this);
        var cell = input.closest('td');
        var place_id = cell.closest('tr').data('place-id');
        var tag_name = input.val();

        // Send an AJAX request to add the tag to the place
        $.ajax({
            url: '/add-tag/',
            type: 'POST',
            data: {
                'place_id': place_id,
                'tag_name': tag_name
            },
            success: function(response) {
                // Add the tag to the cell on success
                cell.append('<span class="tag">' + tag_name + '</span>');
                input.val('');
            },
            error: function(xhr, status, error) {
                // Handle any errors that occur during the AJAX request
                console.error(error);
            }
        });

        console.log("Tag added");
    });
});
