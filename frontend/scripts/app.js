const endpoint = "https://spacex.teewuane.com/api/v1/launchpads";
// const endpoint = "http://127.0.0.1:8000/api/v1/launchpads";

const updateData = () => {
	$.ajax({
			dataType: "json",
			url: endpoint,
			success: (data) => {
				const container = $("#app");
				container.empty();
				$.each(data, (key, val) => {
					$("<div/>", {
						class: `launchpad ${val.status}`,
						html: [
							$("<h3/>", {
								class: 'full-name',
								html: val.full_name
							}),
							$("<div/>", {
								class: 'status',
								html: val.status
							}),
						]
					}).appendTo(container);
				});
			}
		});
}


$(document).ready(function(){
	updateData();
});
