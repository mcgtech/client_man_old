 $(function() {
    setup_dob_datepicker();
    //setup_inline_client_notes();
  });

function setup_dob_datepicker()
{
    var start_year = '1990';
    var start_date = new Date('January 1, ' + start_year);
    $( ".datepicker" ).datepicker({
      changeMonth: true,
      changeYear: true,
      yearRange: start_year + ':' + new Date().getFullYear(),
      defaultDate: start_date,
      //dateFormat: 'dd-mm-yy'
    });
}

function setup_inline_client_notes()
{
    $('#notes tr').formset({
        addText: 'add link',
        deleteText: 'remove',
        prefix: '{{ notes_form_set.nested }}'
    });
}