((function(){$(document).ready(function(){return $("[rel='autocomplete']").autocomplete({source:function(a,b){return $.ajax({type:"GET",url:$(this.element).data("url"),data:{q:$(this.element).val()},dataType:"json",success:function(a){return b(a)}})}})})})).call(this)