$(function () {
    if ($("#f-importer").length) {
        var myDropzone = new Dropzone("#f-importer");
        myDropzone.on("success", function (file, xhr) {
            $("#m-importer").modal("hide");
            item_list()
            if (!xhr.error) {
                swal({
                    title: "Importar Archivo",
                    text: "datos cargados correctamente",
                    icon: "success",
                    buttons: {
                        cancel: {
                            visible: false,
                        },
                        confirm: {
                            text: "Aceptar",
                            value: true,
                            closeModal: true,
                        },
                    },
                });
            } else {
                if (xhr.path) {
                    swal({
                        title: "Importar Archivo",
                        text: "ocurrio un problema",
                        icon: "error",
                        buttons: true,
                        dangerMode: true,
                        buttons: {
                            cancel: {
                                visible: true,
                            },
                            confirm: {
                                text: "Descargar Detalle",
                                value: true,
                                closeModal: true,
                            },
                        },
                    }).then((status) => {
                        if (status) {
                            window.open(xhr.path);
                        }
                    });
                }
                else{
                    swal({
                        title: "Importar Archivo",
                        text: "Error de Formato",
                        icon: "error",
                        buttons: true,
                        dangerMode: true,
                        buttons: {
                            cancel: {
                                visible: false,
                            },
                            confirm: {
                                text: "Aceptar",
                                closeModal: true,
                            },
                        },
                    })
                }
            }
        });

        myDropzone.on("error", function (file, xhr) {
            $("#m-importer").modal("hide");
            $.notify({message: "Ocurrio un Problema: "+xhr.error}, {type: "danger", allow_dismiss:false});
        });

        myDropzone.on("complete", function (file) {
            myDropzone.removeFile(file);
        });
    }
});


jQuery.extend(jQuery.validator.messages, {
    required: "Requerido",
    remote: "Please fix this field.",
    email: "Correo invalido",
    url: "Please enter a valid URL.",
    date: "Please enter a valid date.",
    dateISO: "Please enter a valid date (ISO).",
    number: "Ingrese un número",
    digits: "Please enter only digits.",
    creditcard: "Please enter a valid credit card number.",
    equalTo: "Please enter the same value again.",
    accept: "Archivo con extensión invalida.",
    maxlength: jQuery.validator.format("Máximo {0} caracteres"),
    minlength: jQuery.validator.format("Mínimo {0} caracteres"),
    rangelength: jQuery.validator.format(
        "Please enter a value between {0} and {1} characters long."
    ),
    range: jQuery.validator.format("Please enter a value between {0} and {1}."),
    max: jQuery.validator.format(
        "Please enter a value less than or equal to {0}."
    ),
    min: jQuery.validator.format("Valor min {0}"),
    extension: "Formato invalido",
});

var LoadTable = (function () {
    "use strict";
    return {
        //main function
        init: function (config) {
            var table;
            var language = {
                decimal: ",",
                thousands: ".",
                emptyTable: "Sin Datos",
                info: "mostrando _END_ de _TOTAL_ registros",
                infoEmpty: "0-0 de 0",
                infoFiltered: "",
                infoPostFix: "",
                lengthMenu: "_MENU_",
                loadingRecords: "Cargando...",
                processing: "Procesando...",
                search: "",
                searchPlaceholder: "Buscar",
                zeroRecords: "No se encontraron registros",
                paginate: {
                    first: "Primero",
                    last: "Último",
                    next: ">",
                    previous: "<",
                },
            };

            var buttons = [
                // 'copyHtml5',
                'excel',
                'csvHtml5',
                'pdfHtml5'
            ]

            // var buttons = [
            //     {
            //         text: 'CSV',
            //         extend: 'csv',
            //         className: 'btn-sm'
            //     },
            //     {
            //         text: 'EXCEL',
            //         extend: 'excel',
            //         className: 'btn-sm'
            //     },
            //     {
            //         text: 'PDF',
            //         extend: 'pdf',
            //         className: 'btn-sm'
            //     },
            //     {
            //         text: 'Copiar',
            //         extend: 'copy',
            //         className: 'btn-sm'
            //     },
            //     {
            //         text: 'Imprimir',
            //         extend: 'print',
            //         className: 'btn-sm'
            //     }
            // ]

            // var buttons = [
            //     {
            //         extend: "excel",
            //     },
            //     {
            //         extend: "pdf",
            //     },
            //     // {
            //     //   extend: 'print',
            //     //   customize: function(win) {
            //     //     $(win.document.body).addClass('white-bg');
            //     //     $(win.document.body).css('font-size', '10px');
            //     //     $(win.document.body).find('table').addClass('compact').css('font-size', 'inherit');
            //     //   }
            //     // }
            // ];

            if ($.fn.DataTable.isDataTable(config.id)) {
                table = $(config.id).DataTable();
                table.destroy();
                $(config.id).empty();
            }
            if (config.structure != undefined && $(config.id).length > 0) {
                $(config.id).append(config.structure.tfoot);
            }

            if ($(config.id).length !== 0) {
                table = $(config.id).DataTable({
                    language: language, // lenguaje
                    data: config.data == null ? false : config.data, // filas
                    ajax: config.ajax == null ? false : config.ajax,
                    // cache: config.cache == null ? true : config.cache,
                    deferRender: config.deferRender == null ? false : config.deferRender,
                    order: config.order == null ? [[0, "asc"]] : config.order, // columna a ordenar
                    info: config.info == null ? true : config.info, // info
                    responsive: config.responsive == null ? true : config.responsive,
                    // stateSave: config.stateSave == null ? true: config.stateSave,
                    columns: config.columns == null ? [] : config.columns, // columnas
                    columnDefs: config.columnDefs == null ? [] : config.columnDefs,
                    paginate: config.paginate == null ? true : config.paginate, // paginador
                    pageLength: config.pageLength == null ? 10 : config.pageLength, // elementos a mostar por defecto
                    bLengthChange:
                        config.bLengthChange == null
                            ? true
                            : config.bLengthChange, // elementos a mostrar
                    searching: config.searching == null ? true : config.searching, // buscar
                    searchCols: config.searchCols == null ? [] : config.searchCols, // filtrar por defecto la tabla
                    ordering: config.ordering == null ? true : config.ordering, // ordenar
                    rowCallback:
                        config.rowCallback == null
                            ? function () {}
                            : config.rowCallback,
                    drawCallback:
                        config.drawCallback == null
                            ? function () {}
                            : config.drawCallback,
                    pagingType:
                        config.pagingType == null
                            ? "simple_numbers"
                            : config.pagingType,
                    buttons: config.buttons == null ? buttons : config.buttons,
                    footerCallback:
                        config.footerCallback == null
                            ? function () {}
                            : config.footerCallback,

                    dom: '<"top"lBf>rt<"bottom"ip><"clear">',
                    // buttons: [{
                    //     text: 'CSV',
                    //     extend: 'csv',
                    //     className: 'btn-sm'
                    //   },
                    //   {
                    //     text: 'EXCEL',
                    //     extend: 'excel',
                    //     className: 'btn-sm'
                    //   },
                    //   {
                    //     text: 'PDF',
                    //     extend: 'pdf',
                    //     className: 'btn-sm'
                    //   },
                    //   {
                    //     text: 'Copiar',
                    //     extend: 'copy',
                    //     className: 'btn-sm'
                    //   },
                    //   {
                    //     text: 'Imprimir',
                    //     extend: 'print',
                    //     className: 'btn-sm'
                    //   }
                    // ],
                });
            }
            return table;
        },
    };
})();

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != "") {
        var cookies = document.cookie.split(";");
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == name + "=") {
                cookieValue = decodeURIComponent(
                    cookie.substring(name.length + 1)
                );
                break;
            }
        }
    }
    return cookieValue;
}

function item_delete(data, callback){
    swal({
        title: "¿ Eliminar "+data.name+" ?",
        icon: "warning",
        buttons: {
            cancel: {
                text: "Cancelar",
                visible: true,
                closeModal: true,
            },
            confirm: {
                text: "Aceptar",
                value: true,
            },
        },
    }).then((status) => {
        if (status) {
            $.ajax({
                url: data.url,
                type: 'DELETE',
                headers: { "X-CSRFToken": getCookie("csrftoken") },
                beforeSend: function () {},
                "success": function(response) {
                    $.notify({message: "Eliminado Correctamente"}, {type: "primary", allow_dismiss:false});
                    if (callback)
                        callback()
                },
                error: function(data, textStatus, jqXHR) {
                    $.notify({message: "Ocurrio un Problema"}, {type: "danger", allow_dismiss:false});
                }
            });
        }
    });
}

function form_create(url){
    // open modal
    $("#m-item").modal("show")
    // clear fields
    $("#f-item input[type='text']").val("")
    $("#f-item input[type='number']").val("")
    // clear errors
    $("#f-item .container-error").text("")
    // update action
    $("#f-item").attr("action", url)
    // update method
    $("#f-item").attr("method", "POST")
}


function form_clear(form, fields, errors){
    if (errors){
        $(form+' .container-error').text('')
    }
}

function form_errors(form, errors){
    $.each(errors, function(index, value) {
        // clear
        $(form+" [name="+index+"]").closest('.form-group').find('.container-error').html('')
        // errors
        $(form+" [name="+index+"]").addClass('error')
        $(form+" [name="+index+"]").closest('.form-group').find('.container-error').append(value[0])
    });
}






$(document).ready(function() {
    // errores datatable
    // $.fn.dataTable.ext.errMode = 'none';

    // validate: rut
    $.validator.addMethod("rut", function(value, element) {
        var status = true;
        if (!$.validateRut(value)) {
            status = false
        }
        return status;
    }, 'R.U.T. invalido');

    // // plugins
    // $('.tags-aio').tagsinput();

    // $('.select2-aio').select2({
    //     placeholder: 'Seleccionar',
    //     searchInputPlaceholder: 'Buscar opción',
    // });

    // $('.selectpicker-aio').selectpicker({
    //     selectAllText: 'Todo',
    //     deselectAllText: 'Ninguno',
    //     countSelectedText: '{0} seleccionados de {1}'
    // });

    // // $('.datepicker-aio').datepicker({
    // //     firstDay: 1,
    // //     dayNamesMin: ["Do", "Lu", "Ma", "Mi", "Ju", "Vi", "Sa"],
    // //     monthNames: [ "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
    // //     monthNamesShort: [ "Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic" ],
    // //     dateFormat: "dd/mm/yy",
    // //     changeMonth: true,
    // //     changeYear: true,
    // // });

    // $('.datepicker-aio').datepicker({
    //     format: 'dd/mm/yyyy',
    //     language: 'es'
    // });

    // formats
    $(".format-rut").rut({
        formatOn: 'keyup'
    })


    $('.selectpicker').selectpicker({
        noneSelectedText: "seleccionar",
        countSelectedText: " {0} seleccionados"
    });

    // $('form .custom-file-input').change(function(){
    //     $(this).closest('.custom-file').find('.custom-file-label').text($(this).val())
    // })

    $('.datepicker-as').datepicker({
        format: 'dd/mm/yyyy',
        weekStart: 1,
        language: 'es'
    })

    $('.daterange').daterangepicker({
        opens: 'left',
        locale: {
            format: "DD/MM/YYYY",
            separator: " - ",
            applyLabel: "Actualizar",
            cancelLabel: "Cancelar",
            fromLabel: "From",
            toLabel: "To",
            customRangeLabel: "Custom",
            weekLabel: "W",
            daysOfWeek: [
                "Do",
                "Lu",
                "Ma",
                "Mi",
                "Ju",
                "Vi",
                "Sa"
            ],
            monthNames: [
                "Enero",
                "Febrero",
                "Marzo",
                "Abril",
                "Mayo",
                "Junio",
                "Julio",
                "Agosto",
                "Septiembre",
                "Octubre",
                "Noviembre",
                "Diciembre"
            ],
            firstDay: 1
        }
    });
})
