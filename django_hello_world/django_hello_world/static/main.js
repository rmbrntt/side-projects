/**
 * Created by rmb on 7/17/16.
 */
$(function() {
    console.log("test")

    $("#btn-click").click(function() {
        if ($('input').val() !== '') {
            var input = $("input").val()
            console.log(input)
        }
    });

    $("#form-clear").click(function(e) {
        e.preventDefault()
        $("input").val("");
    });
});