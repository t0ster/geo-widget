$(document).ready ->
  $("[rel='autocomplete']").autocomplete({
      source: (request, response) ->
        $.ajax(
          type: "GET",
          url: $(this.element).data("url"),
          data: {
            q: $(this.element).val()
          },
          dataType: "json",
          success: (data) ->
            response(data)
        )
  })
