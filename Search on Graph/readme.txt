Nghiên cứu, cài đặt và trình bày các thuật toán trên đồ thị: BFS, DFS, UCS, A*. 
Viết code của mỗi thuật toán và đánh giá.
1. Thuật toán BFS:
  - Ý tưởng: Thuật toán xây dựng cây tìm kiếm theo chiều rộng, tức là với mỗi nút gốc được mở ra, ta xét hết nút con (đỉnh kề) của chúng, rồi từ mỗi nút con ta lại xét hết những nút con của nó,… Cứ thế tiếp tục cho đến khi nào chạm phải nút đích (goal) thì dừng lại. Nếu duyệt hết cây mà không có nút đích thì kết luận không tìm thấy đường đi.
  - Ưu điểm: có thể xét duyệt tất cả các đỉnh, nếu đường đi hữu hạn chắc chắn sẽ tìm đến đích
  - Khuyết điểm: mang tính chất vét cạn, không nên sử dụng khi số đỉnh duyệt là quá lớn. Không chú ý thông tin trong đỉnh dẫn đến duyệt nhiều đỉnh thừa không cần thiết.
  
 2. Thuật toán DFS:
  - Ý tưởng: Thuật toán luôn mở rộng nút nằm ở sâu nhất trong nhánh hiện tại đang xét trên cây tìm kiếm. Sau khi đã đến được nút sâu nhất, thuật toán sẽ quay trở lại nút gần nhất có các nút con chưa được xét đến. Nó luôn mở rộng nút theo chiều sâu mãi theo một hướng cho đến khi không thể mở rộng được nữa.
  - Ưu điểm: sử dụng bộ nhớ hiệu quả hơn BFS, tìm kiếm nhanh hơn khi chỉ mở một số lượng các nút nhỏ.
  - Nhược điểm: chỉ lưu lại những trạng thái chưa xét đến, phù hợp cho việc chỉ tìm duy nhất một đường đi cho bài toán. Có thể bị lặp vô hạn trong vài trường hợp. Tránh sử dụng cho những vấn đề mà cây tìm kiếm lớn hoặc độ sâu tối đa không xác định.
  
  3. Thuật toán UCS:
  - Ý tưởng: Thuật toán dùng trong đồ thị có trọng số. Tương tự như BFS, nhưng thay vì mở rộng nút gần nhất thì ta mở rộng nút có chi phí đường đi tới nó thấp nhất. BFS là một dạng đặc biệt của thuật toán này trong trường hợp các bước biến đổi có chi phí như nhau. Trong UCS, thao tác chính trong mỗi vòng lặp là lấy ra nút có chi phí thấp nhất trong
hàng đợi và cập nhật thêm các trạng thái con của nút vừa lấy.
  - Ưu điểm: dùng trong đồ thị có trọng số để tìm được đường đi có chi phí nhỏ nhất.
  - Khuyết điểm: có thể bị lặp vô hạn nếu gặp một nút có chi phí chuyển đổi tới cùng trạng thái đó bằng 0. Tốn bộ nhớ và thời gian tính toán, cập nhật chi phí trên mỗi nút.
  
  4. Thuật toán A*:
    - Ý tưởng: Thuật toán này đánh giá một nút dựa trên chi phí từ nút gốc tới nút đó – g(n), cộng với chi phí từ nút đó đến đích – h(n). 
                                                        f(n) = g(n) + h(n)
      Với f(n) = ước lượng chi phí của lời giải “tốt nhất” qua n, ta sẽ chọn nút có giá trị f(n) nhỏ nhất, sau đó xét tới nút con của nó và tiếp tục chọn nút có giá trị f(n) nhỏ nhất. Do ở mỗi bước ta đã chọn nút “tối ưu” nên đó chính là đường đi “tốt nhất” mà không cần phải xét thêm các nút khác cùng bậc.
   - Ưu điểm: tìm được lời giải “tối ưu” nhất cho đường đi.
   - Khuyết điểm: phụ thuộc vào cách chọn hàm heuristic h(n). Hàm heuristic chấp nhận được không bao giờ vượt quá chi phí để đến đích thật sự thì mới đảm bảo tìm được lời giải tối ưu.
   
   5. Sự khác biệt giữa UCS và A*:
   Điểm khác biệt lớn nhất giữa UCS và A* chính là việc tính chi phí để chọn nút “tối ưu”. UCS chỉ sử dụng chi phí g(n) từ nút gốc tới nút đang xét, còn A* sẽ sử dụng cả chi phí g(n) cộng với h(n) là chi phí từ nút đang xét tới nút đích. Như vậy A* sẽ có được nhiều thông tin hơn về một nút để cho ra đường đi tối ưu.
   Một điểm khác biệt nữa là cách chạy thuật toán. UCS luôn phải lưu lại và cập nhật lại chi phí các nút trong hàng đợi nếu chi phí của nó lớn hơn chi phí từ nút gốc tới nút đang xét. Trong khi đó A* chỉ cần chọn nút có chi phí nhỏ nhất rồi làm mới lại hàng đợi, xét nút kề với nút vừa chọn, mà không cần quan tâm đến các nút cùng cấp bị bỏ qua.
