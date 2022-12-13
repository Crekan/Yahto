$(document).ready(function(){
    console.log('hello world')
    $('#modal-btn').click(function(){
        console.log('working')
        $('.ui.modal')
        .modal('show')
        ;
    })
    $('.ui.dropdown').dropdown()
})

// $(document).ready(function (){
//     $('#model-btn').click(function (){
//         $('.ui.modal')
//         .modal('show')
//         ;
//     })
// })