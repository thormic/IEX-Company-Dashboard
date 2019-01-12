% rebase('base.tpl', title='Python')

<form action="/john" method="post">

<div class="wrapper">
    <div class="row">
	    <div class="col-md-12">
            <select class="custom-select custom-select-lg mb-3" name="company">
            <option selected>Select company</option>
            <option value="{{company}}">{{company}}</option>
            </select>
    	</div>
        Start:<input name="start_date" type="text"><br>
        End:<input name="end_date" type="text">

            <input value="submit" type="submit" />
    </div>
</div>
</form>
