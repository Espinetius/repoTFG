
    var ctx = document.getElementById("progressdays").getContext("2d");
    var MyChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
            datasets: [{
                label: 'Numero de citas',
                data: [20, 36, 51, 10, 9, 78, 64, 18, 78, 85, 11, 3],
                backgroundColor: [
                    'rgb(0, 153, 255, 0.5)',
                    'rgb(163, 0, 204, 0.5)',
                    'rgb(0, 51, 17, 0.5)',
                    'rgb(255, 102, 0, 0.5)',
                    'rgb(179, 179, 0, 0.5)',
                    'rgb(255, 0, 0, 0.5)',
                    'rgb(0, 255, 255, 0.5)',
                    'rgb(204, 51, 0, 0.5)',
                    'rgb(68, 204, 0, 0.5)',
                    'rgb(0, 0, 204, 0.5)',
                    'rgb(102, 0, 102, 0.5)',
                    'rgb(102, 153, 255, 0.5)'
                ]
            }]
        }
    });
