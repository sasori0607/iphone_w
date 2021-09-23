
$('.repairs .choice .low').click(function(){
    $('.repairs .choice .image').each(function() {
        $( this ).removeClass( "background_choice" ).addClass( "background_choice_no_active" )
    })
    $(this).addClass( "background_choice" ).removeClass( "background_choice_no_active" )
    $('.repairs .table table').html(`
          <tr>
            <th>Диагностика iPhone,iPod ( в случае отказа от ремонта)</th>
            <td>250</td>
          </tr>
          <tr>
            <th>Замена дисплейного модуля</th>
            <td>от 350</td>
          </tr>
          <tr>
            <th>Замена дисплея</th>
            <td>от 500</td>
          </tr>
          <tr>
            <th>Замена матрицы</th>
            <td>от 800</td>
          </tr>
          <tr>
            <th>Замена сенсорного стекла</th>
            <td>от 500</td>
          </tr>
          <tr>
            <th>Обновление программного обеспечения в Вашем устройстве</th>
            <td>от 250</td>
          </tr>
          <tr>
            <th>Чистка от пыли</th>
            <td>от 300</td>
          </tr>
          <tr>
            <th>Перенос данных</th>
            <td>от 250</td>
          </tr>
          <tr>
            <th>Перенос телефонной книги</th>
            <td>от 200</td>
          </tr>
          <tr>
            <th>Прошивка</th>
            <td>от 250</td>
          </tr>
          <tr>
            <th>Ребоуллинг чипа</th>
            <td>от 1200</td>
          </tr>
          <tr>
            <th>Создание и настройка Apple- аккунта + установка приложений</th>
            <td>от 200</td>
          </tr>
          <tr>
            <th>Срочный ремонт(до конца дня)</th>
            <td>от 250</td>
          </tr>`)
})

$('.repairs .choice .high').click(function(){
    $('.repairs .choice .image').each(function() {
        $( this ).removeClass( "background_choice" ).addClass( "background_choice_no_active" )
    })
    $(this).addClass( "background_choice" ).removeClass( "background_choice_no_active" )
    $('.repairs .table table').html(`
        <tr>
            <th>Услуга</th>
            <td>Цена</td>
        </tr>
        <tr>
            <th>Диагностика  ( в случае отказа от ремонта)</th>
            <td>250</td>
        </tr>
        <tr>
            <th>Чистка от пыли</th>
            <td>от 600</td>
        </tr>
        <tr>
            <th>Перенос данных</th>
            <td>от 250</td>
        </tr>
        <tr>
            <th>Ребоуллинг</th>
            <td>от 1200</td>
        </tr>
        <tr>
            <th>Срочный ремонт(до конца дня)</th>
            <td>от 250</td>
        </tr>
        <tr>
            <th>Установка ОС на ваш iMac</th>
            <td>Уточнять</td>
        </tr>
    `)
})