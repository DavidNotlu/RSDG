$(document).ready(function(){
    //  Check Radio-box
        $(".rating input:radio").attr("checked", false);
        $('.rating input').click(function () {
            $(".rating span").removeClass('checked');
            $(this).parent().addClass('checked');
        });
    
        $('input:radio').change(
        function(){
            current_user.rating = this.value;
        }); 
    });

function redirect(){
    window.location.href = "/my_drinks_read_only";
}