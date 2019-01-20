% rebase('base.tpl', title='Python')
<div class="container">
    <div class="row">
        <div class="col-lg-12 d-flex align-items-stretch" style=" height: auto" >
            <div class="card border-primary mb-2">
                <div class="card-header">{{!company}}
                </div>
                <div class="card-body text-primary">
                    <h4 class="card-title">{{!description}}</h4>
                </div>
                <div class="card-body text-secondary">
                    <h5 class="card-title">CEO of the company: {{!ceo}}</h5>
                </div>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="card-group col-lg-12">
            <div class="col-lg-3 d-flex align-items-stretch">
                <div class="card border-primary mb-6">
                    <div class="card-body text-secondary">
                        <h4 class="card-title">Company website:</h4>
                        <a href="{{!website}}">
                            <p class="card-text">{{!website}}</p>
                        </a>
                    </div>
                </div>
            </div>
            <div class="col-lg-3 d-flex align-items-stretch">
                <div class="card border-primary mb-6">
                    <div class="card-body text-secondary">
                        <h4 class="card-title">Company sector affiliation:</h4>
                        <p class="card-text">{{!sector}}</p>
                    </div>
                </div>
            </div>
            <div class="col-lg-3 d-flex align-items-stretch">
                <div class="card border-primary mb-6">
                    <div class="card-body text-secondary">
                        <h4 class="card-title">Industry:</h4>
                        <p class="card-text">{{!industry}}</p>
                    </div>
                </div>
            </div>
            <div class="col-lg-3 d-flex align-items-stretch">
                <div class="card border-primary mb-6">
                    <div class="card-body text-secondary">
                        <h4 class="card-title">Type of stock:</h4>
                        <p class="card-text">{{!issuetype}}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <hr style="padding: 20px 0px 20px 0px">

    <div class="row">
        <div class="col-lg-12">
            <h1 style="text-align: center">Aggregated key indicators</h1>
        </div>
    </div>

    <div class="row">
        <div class="card-group col-lg-12">
            <div class="col-lg-6 d-flex align-items-stretch">
                <div class="card border-primary mb-6">
                    <div class="card-body text-primary border">
                        <h4 class="card-title">Highest stock price in the last year:</h4>
                            <h1 class="card-text" style="text-align: center">{{!week52high}}</h1>
                    </div>
                </div>
            </div>
            <div class="col-lg-6 d-flex align-items-stretch">
                <div class="card border-primary mb-6">
                    <div class="card-body text-primary border">
                        <h4 class="card-title">Lowest stock price in the last year:</h4>
                            <h1 class="card-text" style="text-align: center">{{!week52low}}</h1>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="row">
        <div class="card-group col-lg-12">
            <div class="col-lg-6 d-flex align-items-stretch">
                <div class="card border-primary mb-6">
                    <div class="card-body text-primary border">
                        <h4 class="card-title">Market capitalization:</h4>
                            <h1 class="card-text" style="text-align: center">{{!marketcap}}</h1>
                    </div>
                </div>
            </div>
            <div class="col-lg-6 d-flex align-items-stretch">
                <div class="card border-primary mb-6">
                    <div class="card-body text-primary border">
                        <h4 class="card-title">YTD change in the company value:</h4>
                            <h1 class="card-text" style="text-align: center">{{!percent_change}}</h1>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <hr style="padding: 20px 0px 20px 0px">

    <div class="row">
        <div class="col-lg-6">
            <div class="card-body text-primary">
                <h2 style="text-align: center " >Information Table</h2>
                <br>
                <h4 style="text-align: center " >Dates between {{!start_date}} and {{!end_date}}</h4>
            </div>
        </div>
        <div class="col-lg-6">
            <div class="card-body text-primary">
                <h2 style="text-align: center" >Charts</h2>
                <br>
                <h4 style="text-align: center " >Dates between {{!start_date}} and {{!end_date}}</h4>
            </div>
        </div>
    </div>

    <div class="row" id="charts_table">
        <div class="col-lg-6" >
            <div class="table-responsive">
                <div class="table">
                        {{!table}}
                </div>
            </div>
        </div>
        <div class="col-lg-6">
            <div class="chart" id="barplot">
                <script>
                    var graphs = {{!barplot}};
                    Plotly.plot('barplot',graphs,{});
                </script>
            </div>
            <br>
            <div class="chart" id="scatterplot">
                <script>
                    var graphs = {{!scatterplot}};
                    Plotly.plot('scatterplot',graphs,{});
                </script>
            </div>
        </div>
    </div>

    <hr style="padding: 20px 0px 20px 0px">

    <div class="row" id="show_notes">
        <div class="col-lg-12 d-flex align-items-stretch" style=" height: auto" >
            <div class="card border-primary mb-2">
                <h1 style="padding: 15px 15px 15px 15px">Notes:
                </h1>
                <div class="card-body text-primary">
                    <h4 class="card-title">{{!note}}</h4>
                </div>
            </div>
        </div>
    </div>
</div>
