$(document).ready(function(){
	$("#loadmore").on('click',function(){
		var _currentProducts=$(".product-box").length;
		var _limit=$(this).attr('data-limit');
		var _total=$(this).attr('data-total');
		// Start Ajax
		$.ajax({
			url:'/load-more-data',
            // данные которые отрпавляем на сервер:
			data:{
				limit:_limit,
				offset:_currentProducts,
			},
			dataType:'json',
			beforeSend:function(){
				$("#loadmore").attr('disabled',true);
				$(".load-more-icon").addClass('fa-spin');
			},
			success:function(res){
				$("#filteredProducts").append(res.data);
				$("#loadmore").attr('disabled',false);
				$(".load-more-icon").removeClass('fa-spin');

				var _totalShowing=$(".product-box").length;
				if(_totalShowing==_total){
					$("#loadmore").remove();
				}
			}
		});
		// End
	});

	// Варианты товара - цена в зависимости от выбранной опции Цвет и Размер
	$(".choose-size").hide();

	// Show size according to selected color
	$(".choose-color").on('click',function(){
		$(".choose-color").removeClass('focused');
		$(this).addClass('focused');
		var _color=$(this).attr('data-color');

		$(".choose-size").hide();
		$(".color"+_color).show();
		$(".color"+_color).first().addClass('active');

		var _price=$(".color"+_color).first().attr('data-price');
		$(".product-price").text(_price);
	}); //END

		//Show the price according to selected size
		$(".choose-size").on('click',function(){
			$(".choose-size").removeClass('active');
			$(this).addClass('active');

			var _price=$(this).attr('data-price');
			$(".product-price").text(_price);
		})

		//Show the first selected color
		$(".choose-color").first().addClass('focused');
		var _color=$(".choose-color").first().attr('data-color');
		var _price=$(".choose-size").first().attr('data-price');

		$(".color"+_color).show();
		$(".color"+_color).first().addClass('active');
		$(".product-price").text(_price);




		
	// Добавить товар в корзину
	$(document).on('click', ".add-to-cart", function(){
	
		var _vm=$(this);
		var _index=_vm.attr('data-index');
		var _qty=$(".product-qty-"+_index).val();
		var _productId=$(".product-id-"+_index).val();
		var _productImage=$(".product-image-"+_index).val();
		var _productTitle=$(".product-title-"+_index).val();
		var _productPrice=$(".product-price-"+_index).text();

		// Ajax - send request to the server
		$.ajax({
			url:'/cart/add-to-cart', //приложение cart и название пути в тамошнем urls
			data:{
				'id':_productId,
				'image_1':_productImage,
				'qty':_qty,
				'title':_productTitle,
				'price':_productPrice
			},
			dataType:'json',
			beforeSend:function(){
				_vm.attr('disabled',true);
			},
			success:function(res){
				$(".cart-list").text(res.totalitems);
				_vm.attr('disabled',false);
			}
		});
		// End
	});
	// End
		// Delete item from cart
		$(document).on('click','.delete-item',function(){
			var _pId=$(this).attr('data-item');
			var _vm=$(this);
			// Ajax
			$.ajax({
				url:'/cart/delete-from-cart',
				data:{
					'id':_pId,
				},
				dataType:'json',
				beforeSend:function(){
					_vm.attr('disabled',true);
				},
				success:function(res){
					$(".cart-list").text(res.totalitems);
					_vm.attr('disabled',false);
					$("#cartList").html(res.data);
				}
			});
			// End
		});

		// Update item from cart
	$(document).on('click','.update-item',function(){
		var _pId=$(this).attr('data-item');
		var _pQty=$(".product-qty-"+_pId).val();
		var _vm=$(this);
		// Ajax
		$.ajax({
			url:'/cart/update-cart',
			data:{
				'id':_pId,
				'qty':_pQty
			},
			dataType:'json',
			beforeSend:function(){
				_vm.attr('disabled',true);
			},
			success:function(res){
				// $(".cart-list").text(res.totalitems);
				_vm.attr('disabled',false);
				$("#cartList").html(res.data);
			}
		});
		// End
	});

// отсюда
	let switching = false;

function updateGallery() {
  $('.gallery__core img, .gallery__bg img').attr('src',galleryItems[0].url);
  $('.gallery__track').empty();
  $.each(galleryItems,function(index,item){
    $('.gallery__track').append('<div class="gallery__track__item '+(index==0 ? 'active' : '')+'"><img src="'+item.thumb+'" data-full="'+item.url+'" alt=""></div>');
  });
}

function getNewImages() {
  $.get('https://api.unsplash.com/search/photos?client_id=j0z73f4p5WNBe2OK28CHq-GY9kN2GxPj2DpS_bV6nFs&page=1&per_page=9&orientation=squarish&query='+$('.gallery__search input').val(),function(data){
    let items = [];
    $.each(data.results,function(index, item){
      console.log(item);
      let newItem = {
        id: item.id,
        url: item.urls.regular,
        thumb: item.urls.thumb
      }
      items.push(newItem);
    });
    console.log(items);
    galleryItems = items;
    updateGallery();
  });
}

$('.gallery__search input').on('keyup',debounce(() => getNewImages()));
$('.gallery__track').on('click','.gallery__track__item',function(){
  if (!switching) {
    switching = true;
    $(this).addClass('active').siblings().removeClass('active');
    // animate in new core image and background image
    const $oldBGImg = $('.gallery__bg img'); 
    const $oldImg = $('.gallery__core img');
    const newImg = $(this).find('img').data('full');
    const $newImg = $('<img class="slide-in" src="'+newImg+'">');
    const $newBGImg = $('<img class="fade-in" src="'+newImg+'">');
    $('.gallery__core').append($newImg);
    $('.gallery__bg').append($newBGImg);
    setTimeout(function(){
      $newImg.addClass('shift-up');
      $oldImg.addClass('shift-up');
      $oldBGImg.addClass('fade-out');
      $newBGImg.addClass('fading');
      setTimeout(function(){
        $('.gallery__core img').eq(0).remove();
        $('.gallery__bg img').eq(0).remove();
        $('.slide-in').removeClass('slide-in shift-up');
        $('.fade-in').removeClass('fade-in fading');
        switching = false;
      },400);
    },10);
  }
});

let galleryItems = [
    {
        "url": "http://127.0.0.1:8000/media/product_imgs/2022-12-26_230001.jpg",
        "thumb": "http://127.0.0.1:8000/media/product_imgs/2022-12-26_230001.jpg"
    },
    {
        "url": "http://127.0.0.1:8000/media/product_imgs/2022-12-26_231430.jpg",
        "thumb": "http://127.0.0.1:8000/media/product_imgs/2022-12-26_231430.jpg"
    }
];

updateGallery(); // once on load

function debounce(func, timeout = 300){
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => { func.apply(this, args); }, timeout);
  };
}
// и до сюда

const activeImage = document.querySelector(".product-image .active");
const productImages = document.querySelectorAll(".image-list img");
const navItem = document.querySelector('a.toggle-nav');

function changeImage(e) {
  activeImage.src = e.target.src;
}

function toggleNavigation(){
  this.nextElementSibling.classList.toggle('active');
}

productImages.forEach(image => image.addEventListener("click", changeImage));
navItem.addEventListener('click', toggleNavigation);

});

// отсюда открытие большой картинки
$('.portfolio-menu ul li').click(function(){
	$('.portfolio-menu ul li').removeClass('active');
	$(this).addClass('active');
	
	var selector = $(this).attr('data-filter');
	$('.portfolio-item').isotope({
		filter:selector
	});
	return  false;
});
$(document).ready(function() {
var popup_btn = $('.popup-btn');
popup_btn.magnificPopup({
type : 'image',
gallery : {
	enabled : true
}
});
// Конец кода открытия картинки

// слайдер картинок в карточках товаров ТЕСТ

class HvrSlider {
	constructor(selector) {
	  const elements = document.querySelectorAll(selector);
	  elements.forEach((el) => {
		if (el.querySelectorAll('img').length > 1) {
		  const hvr = document.createElement('div');
		  hvr.classList.add('hvr');
  
		  const hvrImages = document.createElement('div');
		  hvrImages.classList.add('hvr__images');
		  hvr.appendChild(hvrImages);
  
		  const hvrSectors = document.createElement('div');
		  hvrSectors.classList.add('hvr__sectors');
		  hvrImages.appendChild(hvrSectors);
  
		  const hvrDots = document.createElement('div');
		  hvrDots.classList.add('hvr__dots');
		  hvr.appendChild(hvrDots);
  
		  el.parentNode.insertBefore(hvr, el);
		  hvrImages.prepend(el);
  
		  const hvrImagesArray = hvr.querySelectorAll('img');
		  hvrImagesArray.forEach(() => {
			hvrSectors.insertAdjacentHTML('afterbegin', '<div class="hvr__sector"></div>');
			hvrDots.insertAdjacentHTML('afterbegin', '<div class="hvr__dot"></div>');
		  });
		  hvrDots.firstChild.classList.add('hvr__dot--active');
		  const setActiveEl = function (targetEl) {
			const index = [...hvrSectors.children].indexOf(targetEl);
			hvrImagesArray.forEach((img, idx) => {
			  if (index == idx) {
				img.style.display = 'block';
			  } else {
				img.style.display = 'none';
			  }
			});
			hvr.querySelectorAll('.hvr__dot').forEach((dot, idx) => {
			  if (index == idx) {
				dot.classList.add('hvr__dot--active');
			  } else {
				dot.classList.remove('hvr__dot--active');
			  }
			});
		  };
		  hvrSectors.addEventListener('mouseover', function (e) {
			if (e.target.matches('.hvr__sector')) {
			  setActiveEl(e.target);
			}
		  });
		  hvrSectors.addEventListener('touchmove', function (e) {
			const position = e.changedTouches[0];
			const target = document.elementFromPoint(position.clientX, position.clientY);
			if (target.matches('.hvr__sector')) {
			  setActiveEl(target);
			}
		  });
		}
	  });
	}
  }
  
  new HvrSlider('.images');
// КОНЕЦ СЛАЙДА КАРТИНОК В КАРТОЧКАХ ТОВАРОВ








});