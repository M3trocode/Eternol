$(document).ready(function() {
    // Function to fetch graph data
    function fetchGraphData() {
        $.ajax({
            url: '/get-graph-data/',
            method: 'GET',
            success: function(response) {
                updateGraph(response.graph_data);
            }
        });
    }

    // Function to update the graph
    function updateGraph(data) {
        const labels = data.map(item => item.substance);
        const pressureData = data.map(item => item.min_pressure);
        const depthData = data.map(item => item.depth_range);

        const ctx = document.getElementById('pressureDepthChart').getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Pressure (psia)',
                    data: pressureData,
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
                }, {
                    label: 'Depth (ft)',
                    data: depthData,
                    backgroundColor: 'rgba(153, 102, 255, 0.2)',
                    borderColor: 'rgba(153, 102, 255, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }

    // Fetch data and update graph on page load
    fetchGraphData();

    // Submit data via AJAX for raw data input
    $('form').on('submit', function(e) {
        e.preventDefault();
        const formData = new FormData(this);

        $.ajax({
            url: '/submit-data/',
            method: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                if (response.status === 'success') {
                    fetchGraphData();  // Refresh graph after new data is submitted
                } else {
                    console.error('Error:', response.error);
                }
            }
        });
    });
});
