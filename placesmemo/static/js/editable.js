$(document).ready(function()  {
    console.log('loaded editable.js');
    // Check if cell is editable
    $(document).on('click', 'td.editable', function() {
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
                    console.log('edit_place event fired')
                    // get CSRF token from cookie
                    const csrftoken = document.cookie.match(/csrftoken=([\w-]+)/)[1];
                
                    // Get the new input value
                    const field = $(this);
                    const value = field.val().trim();
                    const fieldName = $(this).parent().data('field-name');
                    const placeName = $(this).closest('tr').find('td[data-field-name="name"]').text();
                    const placeId = $(this).parent().closest('tr').data('place-id');
                    const payload = {};
                    payload['csrfmiddlewaretoken'] = csrftoken;
                    payload['name'] = placeName;
                    payload[fieldName] = value;
                    payload['id'] = placeId;
                    console.log(payload)
                
                    // send AJAX request to update the Place
                    fetch(`/places/${placeId}/update/`, {
                      method: 'POST',
                      body: JSON.stringify(payload),
                      headers: {'Content-Type': 'application/json', 'X-CSRFToken': csrftoken},
                    })
                    .then(response => response.json())
                    .then(data => {
                      if (data.success) {
                        // update relevant parts of the page with new information
                        // e.g. update the Place name, rating, etc.
                      } else {
                        alert(data.error);
                      }
                    })
                    .catch(error => console.error(error));
                }
            });
        }
    });
});
