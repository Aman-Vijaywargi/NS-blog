## Bootstrap

### Bootstrap Card

Hint: Once check the bootstrap card documentation so that you can find which bootstrap classes can be used and add the link reference of bootstrap. For reference see this
https://getbootstrap.com/docs/5.0/components/card/
Copy the link tag from the below link

```HTML
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
<div class="card">
  <div class="card-header">
    <header>New Features</header>
  </div>
  <div class="card-body">
    <h5 class="card-title">Mobile and Tablet support</h5>
    <p class="card-text">With this new update you will be able to sync your work across large number of platforms.</p>
    <button class="btn btn-primary">Read more</button>
  </div>
  <div class="card-footer">
  </div>
</div>
```

### Bootstrap Buttons

Hint: Once check the bootstrap buttons documentation so that you can find which bootstrap classes can be used. For reference see this
https://getbootstrap.com/docs/5.0/components/buttons/

```HTML
<button class="btn btn-primary" id="button-1">Button-1</button>
<button class="btn btn-outline-secondary" id="button-2">Button-2</button>
<button class="btn btn-info disabled" id="button-6">Button-6</button>
```

### Navigation Bar

Hint: Once check the bootstrap navigation documentation so that you can find which bootstrap classes can be used. For reference see this
https://getbootstrap.com/docs/3.4/components/#nav
And even you need to use the bootstrap classes according to the given description requirements

```HTML
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">
<nav class="navbar navbar-inverse">
  <div class="navbar-header">
  </div>
  <ul class="nav navbar-nav">
    <li>Home</li>
    <li class="dropdown">
      <a href="#dropdown">Dropdown</a>
      <ul class="dropdown-menu">
      </ul>
    </li>
  </ul>
  <form class="navbar-form navbar-left">
  </form>
  <ul class="nav navbar-nav navbar-right">
  </ul>
</nav>
```

### Navigation Bar

Hint: Once check the bootstrap navigation documentation so that you can find which bootstrap classes can be used. For reference see this
https://getbootstrap.com/docs/3.4/components/#nav
And even you need to use the bootstrap classes according to the given description requirements

```HTML
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">
<nav class="navbar navbar-inverse">
  <div class="navbar-header">
  </div>
  <ul class="nav navbar-nav">
    <li>Home</li>
    <li class="dropdown">
      <a href="#dropdown">Dropdown</a>
      <ul class="dropdown-menu">
      </ul>
    </li>
  </ul>
  <form class="navbar-form navbar-left">
  </form>
  <ul class="nav navbar-nav navbar-right">
  </ul>
</nav>
```

### Grid

Hint: Once check the bootstrap grid documentation so that you can find which bootstrap classes can be used. For reference see this
https://getbootstrap.com/docs/5.0/layout/grid/

```HTML
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">
<div class="row">
  <div class="col-sm-1">
    <img src="https://www.thewestindianonline.com/wp-content/uploads/2020/06/Sushant-Singh-Rajput-1-scaled.jpg" alt="Sushant Singh Rajput" width="80" />
  </div>
</div>
```

### Bootstrap Modals

Hint: Once check the bootstrap grid documentation so that you can find which bootstrap classes can be used. For reference see this
https://getbootstrap.com/docs/5.0/components/modal/

```HTML
<button id="open-modal" type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#newton-modal">
  Launch demo modal
</button>
<div class="modal fade" id="newton-modal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
	<div class="modal-dialog modal-dialog-centered">
		<div class="modal-content">
			<div class="modal-header">
				<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
			</div>
			<div class="modal-body">
			</div>
			<div class="modal-footer">
				<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">close</button>
			</div>
		</div>
	</div>
</div>```
