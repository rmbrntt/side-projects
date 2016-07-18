/**
 * Created by rmb on 7/17/16.
 */
$(function() {
    console.log("test")

    $("#btn-click").click(function() {
        if ($('input').val() !== '') {
            var input = $("input").val()
            console.log(input)
            $('ol').append('<li><a href="">x</a> - ' + input + '</li>');
        }
        $('input').val('');
    });

    $("#form-clear").click(function(e) {
        e.preventDefault()
        $("input").val("");
    });
});

$(document).on('click', 'a', function (e) {
    e.preventDefault();
    $(this).parent().remove();
})