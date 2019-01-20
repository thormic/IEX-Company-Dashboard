<!DOCTYPE html>
<html ng-app="MainApp">

<head>
  <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="cache-control" content="max-age=0" />
    <meta http-equiv="cache-control" content="no-cache" />
    <meta http-equiv="expires" content="0" />
    <meta http-equiv="expires" content="Tue, 01 Jan 1980 1:00:00 GMT" />
    <meta http-equiv="pragma" content="no-cache" />
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <link rel="apple-touch-icon" sizes="76x76" href="../static/img/mt.png">
  <!-- ikonka w zakładkach -->
  <link rel="icon" type="image/png" href="../static/img/mt.png">
  <title>
    IEX Company Summarizer
  </title>
  <!--     Fonts and icons     -->
  <link href="https://fonts.googleapis.com/css?family=Poppins:200,300,400,600,700,800" rel="stylesheet" />
  <link href="https://use.fontawesome.com/releases/v5.0.6/css/all.css" rel="stylesheet">
  <!-- Nucleo Icons -->
  <link href="../static/css/nucleo-icons.css" rel="stylesheet" />
  <!-- CSS Files -->
  <link href="../static/css/black-dashboard.css?v=1.0.0" rel="stylesheet" />
  <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.6/d3.min.js"></script>
</head>

<body class="">
  <div class="wrapper">
    <div class="sidebar">
      <div class="sidebar-wrapper">
        <div class="logo">
          <a href="javascript:void(0)" class="simple-text logo-mini">
            BY
          </a>
          <a href="https://s4.scoopwhoop.com/ach/bestie/19.gif" class="simple-text logo-normal">
            Michał Thor
          </a>
        </div>
        <ul class="nav">
          <li>
            <a href="/">
              <i class="tim-icons icon-laptop"></i>
              <p>Choose company</p>
            </a>
          </li>
          <li>
            <a href="/main_dashboard">
              <i class="tim-icons icon-bullet-list-67"></i>
              <p>Dashboard</p>
            </a>
          </li>
          <li>
            <a href="#charts_table">
              <i class="tim-icons icon-chart-bar-32"></i>
              <p>Charts and Table</p>
            </a>
          </li>
          <li>
            <a href="#show_notes">
              <i class="tim-icons icon-book-bookmark"></i>
              <p>Show notes</p>
            </a>
          </li>
          <li>
            <a href="/note">
              <i class="tim-icons icon-notes"></i>
              <p>Add notes</p>
            </a>
          </li>
          <li>
            <a href="/update">
              <i class="tim-icons icon-upload"></i>
              <p>Update company database</p>
            </a>
          </li>
        </ul>
      </div>
    </div>
    <div class="main-panel">
      <!-- Navbar -->
      <nav class="navbar navbar-expand-lg navbar-absolute navbar-transparent">
        <div class="container-fluid">
          <div class="navbar-wrapper" style="padding: 20px 0px 0px 0px">
            <div class="navbar-toggle d-inline">
              <button type="button" class="navbar-toggler">
                <span class="navbar-toggler-bar bar1"></span>
                <span class="navbar-toggler-bar bar2"></span>
                <span class="navbar-toggler-bar bar3"></span>
              </button>
            </div>
            <a class="navbar-brand" href="/">IEX Company Summarizer</a>
          </div>
        </div>
      </nav>
      <!-- End Navbar -->
      <div class="content">
        {{!base}}
      </div>
      <footer class="footer" style="bottom:0; width: 100%; display: inline-block;">
        <div class="container-fluid">
          <ul class="nav">
            <li class="nav-item">
              <a href="javascript:void(0)" class="nav-link">
                IEX Trading Summarize
              </a>
            </li>
            <li class="nav-item">
              <a href="javascript:void(0)" class="nav-link">
                About Me
              </a>
            </li>
            <li class="nav-item">
              <a href="javascript:void(0)" class="nav-link">
                Licenses
              </a>
            </li>
          </ul>
          <div class="copyright">
            ©
            <script>
              document.write(new Date().getFullYear())
            </script> made by
            <a href="javascript:void(0)" style="color:white">Michał Thor</a>
          </div>
        </div>
      </footer>
    </div>
  </div>
  <!--   Core JS Files   -->
  <script src="../static/js/core/jquery.min.js"></script>
  <script src="../static/js/core/popper.min.js"></script>
  <script src="../static/js/core/bootstrap.min.js"></script>
  <script src="../static/js/plugins/perfect-scrollbar.jquery.min.js"></script>
  <!-- Chart JS -->
  <script src="../static/js/plugins/chartjs.min.js"></script>
  <!--  Notifications Plugin    -->
  <script src="../static/js/plugins/bootstrap-notify.js"></script>
  <!-- Control Center for Black Dashboard: parallax effects, scripts for the example pages etc -->
  <script src="../static/js/black-dashboard.min.js?v=1.0.0"></script>
  <!-- Black Dashboard DEMO methods, don't include it in your project! -->
  <script src="../static/demo/demo.js"></script>
  <script>
    $(document).ready(function() {
      // Javascript method's body can be found in static/js/demos.js
      demo.initDashboardPageCharts();

    });
  </script>

</body>

</html>
