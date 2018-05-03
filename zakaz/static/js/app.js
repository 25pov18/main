$(function() {
    /* Сообщения */
    var messages = {
        errors: {
            timeout: 'Время ожидания ответа от сервера истекло.',
            default: 'Произошла непредвиденная ошибка.'
        }
    };

    /* Отправляет форму асинхронно */
    $.fn.ajaxForm = function(options) {
        this.each(function() {
            var $this   = $(this),
                wait    = $this.data('wait'),
                $submit = $(':submit', $this);
            
            var parameters = $.extend({
                url:  $this.attr('action'),
                type: $this.attr('method'),
                context: $this,
                beforeSend: function() {
                    // Блокируем кнопку отправки
                    $submit.prop('disabled', true);
                    
                    $('.has-error :input', $this).trigger('keyup');
                    
                    $this.siblings('.alert-danger')
                         .remove();
                    
                    // Если есть сообщение ожидания
                    if (wait) {
                        $('<span/>', {
                            'class': 'loader',
                            text:  wait
                        }).insertBefore($submit);
                    }
                },
                complete: function() {
                    // Разблокируем кнопку отправки
                    $submit.prop('disabled', false);

                    // Удаляем сообщение ожидания
                    $('.loader', $this).remove();
                },
                success: function(response) {
                    // Если нужно перенаправить
                    if (response.redirect) {
                        window.location.href = response.redirect;
                    }
                },
                error: function(response) {
                    if (response.status !== 422) {
                        return $.ajaxSettings.error(response);
                    }
                    
                    var errors = response.responseJSON;
                    
                    if ($this.data('alert')) {
                        return alert($.toArray(errors).join('\n'));
                    }

                    // Обходим массив ошибок
                    $.each(errors, function(key, error) {
                        // Объект обёртки поля с ошибкой
                        var $group = $('[name='+ key +']:visible', $this).parents('.form-group');

                        // Если поля нет
                        if (!$group.length) {
                            return $('<p/>', {
                                'class': 'alert alert-danger',
                                text: error
                            }).insertBefore($this);
                        }
                        
                        // Описание ошибки
                        $('<span/>', {
                            'class': 'help-block',
                            text: error
                        }).appendTo($group);
                        
                        $group.addClass('has-error');
                    });
                }
            }, options);
            
            // При отправке формы
            $this.on('submit', function() {
                event.preventDefault();
                
                $.extend(parameters, {
                    data: $(this).serializeArray()
                });
                
                $.ajax(parameters);
            });
        });
    };
    
    /* Настройки ajax-запросов */
    $.ajaxSetup({
        timeout: 120000,
        error: function(xhr) {
            var status = xhr.statusText;
            
            if (status == 'abort') {
                return;
            }
                
            var key = messages.errors[status] ? status : 'default';
            
            alert(messages.errors[key]);
        }
    });

    $('[data-toggle="tooltip"]').tooltip();

    // При отправке ajax-форм
    $('[data-toggle=async]').ajaxForm();

    $(document).ajaxStart(function () {
        $('[data-enabled=only-idle]').prop('disabled', true);
    });
    $(document).ajaxStop(function () {
        $('[data-enabled=only-idle]').prop('disabled', false);
    });

    function submitForm(sender) {
        var form = sender.closest('form');
        var element = sender;
        var relatedElements = $(sender.data('related-elements'));
        var itemRoot = sender.closest(sender.data('item-root'));
        var newContainer = $(form.data('move-on-success'));
        var containerToReload = $(sender.data('reload-on-success'));
        var formData = form.serialize();

        element.prop('disabled', true);
        relatedElements.prop('disabled', true);

        $.ajax({
            type: form.attr('method'),
            url: form.attr( 'action'),
            data: formData,
            complete: function( response ) {
                element.prop('disabled', false);
                relatedElements.prop('disabled', false);
            },
            success: function(result) {
                if (itemRoot.length) {
                    if (newContainer.length) {
                        itemRoot.detach().appendTo(newContainer);
                    }
                }
                if (containerToReload.length) {
                    reloadContainer(containerToReload);
                }
                if (result.updatedElements) {
                    $.each(result.updatedElements, function (i, item) {
                        $(item.selector).html(item.html);
                    });
                }
            }
        });
    }

    function reloadContainer(container) {
        var url = container.data('href');

        $.get({
            url: url,
            success: function(html) {
                container.find('[aria-describedby]').tooltip('hide');

                container.html(html);
            }
        });
    }

    function submitFormSync(sender) {
        var form = sender.closest('form');
        var element = sender;
        var method = element.data('form-method');
        var action = element.data('form-action');

        if (method) {
            form.attr('method', method);
        }
        if (action) {
            form.attr('action', action);
        }

        form.submit();
    }
    
    $('[data-onchange=submit]').change(function () {
        submitForm($(this));
    });

    $('[data-onchange=submit-sync]').change(function () {
        submitFormSync($(this));
    });

    $('[data-submit=async]').on('submit', 'form', function () {
        event.preventDefault();

        submitForm($(this));
    });

    $('.all-checkbox').change(function () {
        var relatedElements = $($(this).data('related-elements'));
        relatedElements.prop('checked', $(this).prop('checked'));
    });

    $('[data-role=loader]').click(function () {
        var element = $(this);
        var outputElement = element.siblings('[data-role=output]');

        var isOpened = outputElement.data('opened') === 'true';

        if (isOpened) {
            outputElement.hide();
            outputElement.data('opened', 'false');
        } else {
            element.prop('disabled', true);

            var loadingIndicator = element.siblings('.loading-indicator');
            loadingIndicator.show();

            $.ajax({
                type: 'get',
                url: element.data('href'),
                global: false,
                success: function (html) {
                    outputElement.html(html);
                    outputElement.show();
                    outputElement.data('opened', 'true');
                },
                complete: function () {
                    element.prop('disabled', false);
                    loadingIndicator.hide();
                }
            });
        }
    });

    /*
     * Загрузка дочерних записей
     *
     * Параметры текущего элемента:
     *     data-href - адрес, по которому доступен список дочерних
     *     data-target - указатель элемента, в который добавить загруженные значения
     */
    $('[data-toggle=branch]').on('change', function() {
        var $this     = $(this),
            $option   = $(':selected', $this),
            parent_id = parseInt(
                $option.data('id') || $this.val()
            ),
            url         = $this.data('base') +'/'+ parent_id,
            $target     = $(
                $this.data('target')
            );

        // Блокировка списка
        $target.prop('disabled', true)
               .prop('selectedIndex', 0);

        if (!parent_id) {
            $target.trigger('change');
            
            return;
        }
        
        // Загрузка данных
        $.getJSON(url, function(response) {
            var options = [
                $(':first', $target)
            ];
            
            $.each(response, function(key, entity) {
                var $option = $('<option/>', {
                    value: entity.id,
                    text: entity.name
                });

                if (entity.true_id) {
                    $option.data('id', entity.true_id);
                }
                
                options.push($option);
            });
            
            $target.html(options)
                   .prop('disabled', false)
                   .trigger('change');
        });
    });

    /*
     * При клике на элемент, для действия которого требуется подтверждение
     */
    $('[data-push=confirm]').on('click submit', function(event) {        
        if (!confirm('Подтверждаете действие?')) {
            event.stopImmediatePropagation();
            
            return false;
        }
    });

    // Запуск всплывающих подсказок
    $('body').tooltip({
        selector: '[title]',
        container: 'body'
    });
});
